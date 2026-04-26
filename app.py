import os
import json
import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, render_template, request, session
from logic import (STAGE1_QUESTIONS, STAGE2_QUESTIONS,
                   get_condition_from_stage1, calculate_final_result)
from datetime import datetime

app = Flask(__name__)
app.secret_key = "mentalhealthapp2024"

# ✅ Google Sheets connection
def get_sheet():
    try:
        creds_json = os.getenv("GOOGLE_CREDENTIALS")
        if creds_json:
            creds_dict = json.loads(creds_json)
        else:
            with open("credentials.json") as f:
                creds_dict = json.load(f)

        scopes = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(
            os.getenv("SHEET_ID", "19Cctu7y0ZwZFrLY3U6zJQ6N1I4yP23-XxoD7EuckvIM")
        )
        return sheet.sheet1
    except Exception as e:
        print(f"Sheet error: {e}")
        return None

def save_to_sheet(row):
    try:
        sheet = get_sheet()
        if sheet:
            sheet.append_row(row)
            print("✅ Saved to Google Sheet!")
        else:
            print("❌ Sheet connection failed")
    except Exception as e:
        print(f"Save error: {e}")

# ✅ Routes
@app.route('/')
def index():
    session.clear()
    return render_template('details.html')

@app.route('/save_details', methods=['POST'])
def save_details():
    session['name']  = request.form.get('name', '').strip()
    session['email'] = request.form.get('email', '').strip()
    session['phone'] = request.form.get('phone', '').strip()
    session['dob']   = request.form.get('dob', '').strip()
    session['city']  = request.form.get('city', '').strip()
    session['date']  = request.form.get('date', '').strip()
    return render_template('choose_doctor.html')

@app.route('/stage1')
def stage1():
    doctor = request.args.get('doctor', 'male')
    session['doctor'] = doctor
    return render_template('stage1.html',
                           questions=STAGE1_QUESTIONS,
                           doctor=doctor)

@app.route('/stage1_submit', methods=['POST'])
def stage1_submit():
    answers = {q['id']: request.form.get(q['id'], '') for q in STAGE1_QUESTIONS}
    session['stage1_answers'] = answers
    condition = get_condition_from_stage1(answers)
    session['condition'] = condition
    stage2_questions = STAGE2_QUESTIONS.get(condition, STAGE2_QUESTIONS['stress'])
    session['stage2_questions'] = stage2_questions
    return render_template('stage2.html',
                           questions=stage2_questions,
                           condition=condition,
                           doctor=session.get('doctor', 'male'))

@app.route('/stage2_submit', methods=['POST'])
def stage2_submit():
    stage2_questions = session.get('stage2_questions', [])
    condition = session.get('condition', 'neutral')
    answers = {q['id']: request.form.get(q['id'], '') for q in stage2_questions}
    result = calculate_final_result(condition, answers, stage2_questions)

    # Get all session data
    doctor = session.get('doctor', 'male')
    doctor_name = 'Dr. Harshit' if doctor == 'male' else 'Dr. Insha'
    stage1_answers = session.get('stage1_answers', {})

    # Format stage 1 answers nicely
    s1_formatted = " | ".join([f"{k}: {v}" for k, v in stage1_answers.items()])
    s2_formatted = " | ".join([f"{k}: {v}" for k, v in answers.items()])

    # ✅ Save everything to Google Sheet
    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Timestamp
        session.get('name', 'N/A'),                     # Name
        session.get('email', 'N/A'),                    # Email
        session.get('phone', 'N/A'),                    # Phone
        session.get('dob', 'N/A'),                      # Date of Birth
        session.get('city', 'N/A'),                     # City
        session.get('date', 'N/A'),                     # Assessment Date
        doctor_name,                                     # Doctor chosen
        result['condition'],                             # Condition
        result['severity'],                              # Severity
        result['explanation'],                           # Explanation
        s1_formatted,                                    # Stage 1 answers
        s2_formatted,                                    # Stage 2 answers
        " | ".join(result['solutions'])                  # Solutions
    ]

    save_to_sheet(row)

    return render_template('result.html',
                           result=result,
                           doctor=doctor)

if __name__ == '__main__':
    app.run(debug=True)