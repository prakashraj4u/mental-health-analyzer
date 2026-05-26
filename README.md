# 🧠 Mental Health Analyzer

A Flask-based web application that helps users assess their mental health through a guided two-stage questionnaire. It identifies potential conditions (depression, anxiety, or stress), determines severity, and provides personalised, actionable solutions — all while securely saving results to Google Sheets.

> ⚠️ **Disclaimer:** This app is for informational and self-awareness purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. If you are in distress, please contact a qualified mental health professional.

---

## Features

- **Two-Stage Assessment** — A smart questionnaire that first screens for the most likely condition, then asks targeted follow-up questions specific to that condition.
- **Condition Detection** — Identifies whether the user is experiencing symptoms of depression, anxiety, stress, or is in a neutral/healthy state.
- **Severity Scoring** — Classifies results as Mild, Moderate, or Severe based on scored responses.
- **Personalised Solutions** — Provides practical, condition-specific and severity-specific recommendations for each user.
- **Doctor Persona Selection** — Users can choose a doctor persona (Dr. Harshit or Dr. Insha) for a more personal experience.
- **Google Sheets Integration** — All assessment results are automatically saved to a Google Sheet for record-keeping and analysis.
- **User Details Collection** — Captures name, email, phone, date of birth, city, and assessment date before the assessment begins.

---

## How It Works

The assessment follows a clear flow:

```
User Details → Choose Doctor → Stage 1 (Screening) → Stage 2 (Targeted) → Result + Solutions
```

**Stage 1** asks 7 general questions covering sleep, mood, energy, interest, appetite, nervousness, and overwhelm. Based on the scored responses, the app determines the most likely condition.

**Stage 2** then asks 4 deeper questions specific to the identified condition (e.g., hopelessness and concentration for depression; racing heart and avoidance for anxiety; overwhelm and irritability for stress).

The final result includes the condition, severity level, a plain-language explanation, a list of practical solutions, and an encouraging closing message.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Assessment Logic | Custom rule-based scoring (`logic.py`) |
| Data Storage | Google Sheets via `gspread` |
| Auth | Google Service Account (`google-auth`) |
| Frontend | HTML, CSS (Jinja2 templates) |
| Session Management | Flask server-side sessions |

---

## Project Structure

```
mental-health-analyzer/
├── app.py              # Flask routes and Google Sheets integration
├── logic.py            # All questions, scoring logic, conditions, and solutions
├── requirements.txt    # Python dependencies
├── credentials.json    # Google Service Account key (not committed — use env var)
├── .gitignore
├── static/             # CSS and static assets
└── templates/
    ├── details.html        # User info form
    ├── choose_doctor.html  # Doctor persona selection
    ├── stage1.html         # Screening questionnaire
    ├── stage2.html         # Targeted questionnaire
    └── result.html         # Assessment result and solutions
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- A Google Cloud project with the **Google Sheets API** and **Google Drive API** enabled
- A Google Service Account with access to a target Google Sheet

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prakashraj4u/mental-health-analyzer.git
   cd mental-health-analyzer
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google Sheets credentials:**

   Option A — Using a file (local development):
   - Download your service account key from Google Cloud Console and save it as `credentials.json` in the project root.
   - Share your Google Sheet with the service account email (with Editor access).

   Option B — Using an environment variable (recommended for deployment):
   ```bash
   export GOOGLE_CREDENTIALS='<paste the entire JSON content here>'
   export SHEET_ID='your_google_sheet_id'
   ```

### Running the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## Google Sheet Output

Each completed assessment saves the following columns to your sheet:

| Column | Description |
|---|---|
| Timestamp | Date and time of the assessment |
| Name | User's full name |
| Email | User's email address |
| Phone | User's phone number |
| Date of Birth | User's DOB |
| City | User's city |
| Assessment Date | Date selected by the user |
| Doctor | Dr. Harshit or Dr. Insha |
| Condition | Depression / Anxiety / Stress / Neutral |
| Severity | Mild / Moderate / Severe |
| Explanation | Plain-language result summary |
| Stage 1 Answers | All screening question responses |
| Stage 2 Answers | All targeted question responses |
| Solutions | Recommended actions |

---

## Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_CREDENTIALS` | Full JSON content of the Google Service Account key |
| `SHEET_ID` | The ID of the target Google Sheet (from its URL) |

---

## Conditions & Scoring

The app detects three conditions plus a neutral state:

- **Depression** — Triggered by high scores on mood, sleep, energy, interest, and appetite questions
- **Anxiety** — Triggered by high scores on nervousness and worry questions
- **Stress** — Triggered by high scores on overwhelm and irritability questions
- **Neutral** — All scores are zero; user appears to be in good mental health

Severity is based on total Stage 2 score: **0–4 → Mild**, **5–8 → Moderate**, **9+ → Severe**.

---

## Crisis Support

If you or someone you know needs immediate help, please reach out:

- **iCall India:** 9152987821
- **Vandrevala Foundation (24/7):** 1860-2662-345
- **NIMHANS:** 080-46110007

---

## License

This project is open source. Feel free to fork, modify, and use it.
