from flask import Flask, render_template, request, session
from logic import (STAGE1_QUESTIONS, STAGE2_QUESTIONS,
                   get_condition_from_stage1, calculate_final_result)

app = Flask(__name__)
app.secret_key = "mentalhealthapp2024"

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/stage1')
def stage1():
    return render_template('stage1.html', questions=STAGE1_QUESTIONS)

@app.route('/stage1_submit', methods=['POST'])
def stage1_submit():
    answers = {q['id']: request.form.get(q['id'], '') for q in STAGE1_QUESTIONS}
    session['stage1_answers'] = answers
    condition = get_condition_from_stage1(answers)
    session['condition'] = condition
    stage2_questions = STAGE2_QUESTIONS.get(condition, STAGE2_QUESTIONS['stress'])
    session['stage2_questions'] = stage2_questions
    return render_template('stage2.html', questions=stage2_questions, condition=condition)

@app.route('/stage2_submit', methods=['POST'])
def stage2_submit():
    stage2_questions = session.get('stage2_questions', [])
    condition = session.get('condition', 'neutral')
    answers = {q['id']: request.form.get(q['id'], '') for q in stage2_questions}
    result = calculate_final_result(condition, answers, stage2_questions)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)