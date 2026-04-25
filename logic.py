STAGE2_QUESTIONS = {
    "depression": [
        {"id": "s2q1", "text": "How often do you feel empty or hopeless?",
         "options": ["Never", "Sometimes", "Often", "Always"],
         "scores": [0, 1, 2, 3]},
        {"id": "s2q2", "text": "Do you have trouble concentrating on things?",
         "options": ["Never", "Sometimes", "Often", "Always"],
         "scores": [0, 1, 2, 3]},
        {"id": "s2q3", "text": "Do you feel worthless or guilty for no reason?",
         "options": ["Never", "Sometimes", "Often", "Always"],
         "scores": [0, 1, 2, 3]},
        {"id": "s2q4", "text": "Have you had thoughts of harming yourself?",
         "options": ["Never", "Rarely", "Sometimes", "Often"],
         "scores": [0, 1, 2, 3]},
    ],
    "anxiety": [
        {"id": "s2q1", "text": "Do you feel nervous or on edge frequently?",
         "options": ["Never", "Sometimes", "Often", "Always"],
         "scores": [0, 1, 2, 3]},
        {"id": "s2q2", "text": "Do you have trouble controlling your worries?",
         "options": ["Never", "Sometimes", "Often", "Always"],
         "scores": [0, 1, 2, 3]},
        {"id": "s2q3", "text": "Do you experience a racing heart or shortness of breath?",
         "options": ["Never", "Sometimes", "Often", "Always"],
         "scores": [0, 1, 2, 3]},
        {"id": "s2q4", "text": "Do you avoid situations because of fear or worry?",
         "options": ["Never", "Sometimes", "Often", "Always"],
         "scores": [0, 1, 2, 3]},
    ],
    "stress": [
        {"id": "s2q1", "text": "Do you feel overwhelmed by responsibilities?",
         "options": ["Never", "Sometimes", "Often", "Always"],
         "scores": [0, 1, 2, 3]},
        {"id": "s2q2", "text": "Do you have difficulty relaxing even on days off?",
         "options": ["Never", "Sometimes", "Often", "Always"],
         "scores": [0, 1, 2, 3]},
        {"id": "s2q3", "text": "Do you experience headaches or muscle tension?",
         "options": ["Never", "Sometimes", "Often", "Always"],
         "scores": [0, 1, 2, 3]},
        {"id": "s2q4", "text": "Do you feel irritable or short-tempered?",
         "options": ["Never", "Sometimes", "Often", "Always"],
         "scores": [0, 1, 2, 3]},
    ]
}

SOLUTIONS = {
    "depression": {
        "mild": [
            "Take a 20-minute walk outside every day — sunlight boosts mood naturally",
            "Write 3 things you are grateful for every morning in a journal",
            "Reach out to one friend or family member today just to talk",
            "Maintain a regular sleep schedule — sleep and wake at the same time",
            "Reduce social media usage to less than 30 minutes per day",
        ],
        "moderate": [
            "Consider speaking to a counsellor or therapist — it really helps",
            "Join a hobby group or community activity to stay socially connected",
            "Exercise for at least 30 minutes 3 times a week",
            "Avoid alcohol and processed foods — they worsen low mood",
            "Practice mindfulness meditation using free apps like Headspace",
        ],
        "severe": [
            "Please speak to a mental health professional as soon as possible",
            "Contact a helpline — iCall India: 9152987821",
            "Tell a trusted person how you are feeling today",
            "Remove access to anything that could be used for self-harm",
            "Remember: depression is treatable — you will feel better with help",
        ]
    },
    "anxiety": {
        "mild": [
            "Practice deep breathing — inhale 4 seconds, hold 4, exhale 4 seconds",
            "Limit caffeine and energy drinks — they trigger anxiety",
            "Write down your worries and challenge each one with facts",
            "Exercise daily — it reduces anxiety hormones naturally",
            "Establish a calming bedtime routine to improve sleep",
        ],
        "moderate": [
            "Try progressive muscle relaxation exercises daily",
            "Consider speaking to a therapist about CBT (Cognitive Behavioural Therapy)",
            "Gradually face situations you avoid — avoidance makes anxiety worse",
            "Reduce news and social media consumption significantly",
            "Practice yoga or tai chi — both are proven to reduce anxiety",
        ],
        "severe": [
            "Please consult a doctor or psychiatrist — medication may help",
            "Contact iCall India: 9152987821 for immediate support",
            "Don't face severe anxiety alone — tell someone you trust today",
            "Avoid making big life decisions when anxiety is at its peak",
            "Remember: anxiety is very treatable — many people recover fully",
        ]
    },
    "stress": {
        "mild": [
            "Make a daily to-do list and prioritise only 3 most important tasks",
            "Take 5-minute breaks every hour when working or studying",
            "Spend time in nature — even a 15-minute walk helps significantly",
            "Say no to commitments that overwhelm your schedule",
            "Spend time doing one thing you genuinely enjoy every day",
        ],
        "moderate": [
            "Identify your top stressors and create a plan to address each one",
            "Talk to your manager, teacher or mentor about your workload",
            "Practice time management techniques like the Pomodoro method",
            "Exercise regularly — it is the best stress relief tool available",
            "Consider speaking to a counsellor about stress management",
        ],
        "severe": [
            "Take a break from work or study — burnout is a serious condition",
            "Speak to a doctor — chronic stress affects physical health too",
            "Contact iCall India: 9152987821 for professional guidance",
            "Eliminate or delegate as many responsibilities as possible right now",
            "Prioritise sleep above everything — rest is not a luxury, it is medicine",
        ]
    },
    "neutral": {
        "mild": [
            "Keep up your healthy habits — you are doing great!",
            "Continue exercising regularly to maintain your wellbeing",
            "Stay socially connected with friends and family",
            "Practice mindfulness to stay mentally sharp",
            "Check in with yourself regularly to monitor your mental health",
        ]
    }
}

STAGE1_QUESTIONS = [
    {"id": "q1", "text": "How would you rate your sleep quality lately?",
     "options": ["Very good", "Good", "Average", "Poor", "Very poor"],
     "scores": [0, 0, 1, 2, 3]},
    {"id": "q2", "text": "How often do you feel sad or hopeless?",
     "options": ["Never", "Rarely", "Sometimes", "Often", "Always"],
     "scores": [0, 0, 1, 2, 3]},
    {"id": "q3", "text": "Do you feel tired even after resting?",
     "options": ["Never", "Sometimes", "Yes, frequently"],
     "scores": [0, 1, 2]},
    {"id": "q4", "text": "Have you lost interest in things you used to enjoy?",
     "options": ["Not at all", "A little", "Quite a lot", "Completely"],
     "scores": [0, 1, 2, 3]},
    {"id": "q5", "text": "How is your appetite lately?",
     "options": ["Normal", "Eating more than usual", "Eating less than usual", "No appetite at all"],
     "scores": [0, 1, 2, 3]},
    {"id": "q6", "text": "Do you feel nervous or on edge?",
     "options": ["Never", "Sometimes", "Often", "Always"],
     "scores": [0, 1, 2, 3]},
    {"id": "q7", "text": "Do you feel overwhelmed by daily tasks?",
     "options": ["Never", "Sometimes", "Often", "Always"],
     "scores": [0, 1, 2, 3]},
]

def get_condition_from_stage1(answers):
    depression_score = 0
    anxiety_score = 0
    stress_score = 0

    score_map = {
        "q1": {"Very good": 0, "Good": 0, "Average": 1, "Poor": 2, "Very poor": 3},
        "q2": {"Never": 0, "Rarely": 0, "Sometimes": 1, "Often": 2, "Always": 3},
        "q3": {"Never": 0, "Sometimes": 1, "Yes, frequently": 2},
        "q4": {"Not at all": 0, "A little": 1, "Quite a lot": 2, "Completely": 3},
        "q5": {"Normal": 0, "Eating more than usual": 1, "Eating less than usual": 2, "No appetite at all": 3},
        "q6": {"Never": 0, "Sometimes": 1, "Often": 2, "Always": 3},
        "q7": {"Never": 0, "Sometimes": 1, "Often": 2, "Always": 3},
    }

    depression_score = (score_map["q1"].get(answers.get("q1",""), 0) +
                        score_map["q2"].get(answers.get("q2",""), 0) +
                        score_map["q3"].get(answers.get("q3",""), 0) +
                        score_map["q4"].get(answers.get("q4",""), 0) +
                        score_map["q5"].get(answers.get("q5",""), 0))

    anxiety_score = score_map["q6"].get(answers.get("q6",""), 0) * 2
    stress_score = score_map["q7"].get(answers.get("q7",""), 0) * 2

    if depression_score == 0 and anxiety_score == 0 and stress_score == 0:
        return "neutral"
    if depression_score >= anxiety_score and depression_score >= stress_score:
        return "depression"
    elif anxiety_score >= stress_score:
        return "anxiety"
    else:
        return "stress"

def get_severity(score):
    if score <= 4:
        return "mild"
    elif score <= 8:
        return "moderate"
    else:
        return "severe"

def calculate_final_result(condition, stage2_answers, stage2_questions):
    total_score = 0
    for q in stage2_questions:
        answer = stage2_answers.get(q["id"], "")
        idx = q["options"].index(answer) if answer in q["options"] else 0
        total_score += q["scores"][idx]

    if condition == "neutral":
        severity = "mild"
    else:
        severity = get_severity(total_score)

    solutions = SOLUTIONS.get(condition, SOLUTIONS["neutral"]).get(severity, [])

    explanations = {
        ("depression", "mild"): "Your answers suggest you may be experiencing mild low mood. This is common and manageable with some lifestyle changes.",
        ("depression", "moderate"): "Your responses indicate moderate signs of depression. It's important to take this seriously and seek some support.",
        ("depression", "severe"): "Your answers suggest significant depression. Please reach out to a mental health professional as soon as possible.",
        ("anxiety", "mild"): "You seem to be experiencing mild anxiety. Small daily habits can make a big difference.",
        ("anxiety", "moderate"): "Your responses suggest moderate anxiety. Consider speaking to someone you trust or a professional.",
        ("anxiety", "severe"): "Your answers indicate significant anxiety. Please seek professional support — effective treatments are available.",
        ("stress", "mild"): "You are experiencing mild stress. Some simple changes to your routine can help greatly.",
        ("stress", "moderate"): "Your responses suggest moderate stress levels. It's time to address the sources of stress in your life.",
        ("stress", "severe"): "Your answers indicate high stress or burnout. Please prioritise your wellbeing urgently.",
        ("neutral", "mild"): "Great news! Your responses suggest you are in a good mental state. Keep up your healthy habits!",
    }

    explanation = explanations.get(
        (condition, severity),
        "Based on your answers, we have identified some areas to focus on for your wellbeing."
    )

    closings = {
        "depression": "Remember — you are not alone. Millions of people experience depression and recover fully. Taking this assessment was a brave first step. 💙",
        "anxiety": "Anxiety is one of the most treatable mental health conditions. With the right support, you can feel calm and in control again. 💚",
        "stress": "Stress is a signal that something needs to change. You have the strength to make those changes. Take it one day at a time. 🌟",
        "neutral": "You are doing wonderfully! Keep taking care of yourself and check in regularly. 😊"
    }

    return {
        "condition": condition.capitalize(),
        "severity": severity.capitalize(),
        "explanation": explanation,
        "solutions": solutions,
        "closing": closings.get(condition, "Take care of yourself. You matter. 💙"),
        "score": total_score
    }