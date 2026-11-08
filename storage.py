import json
from pathlib import Path
from quiz import Quiz

STATE_FILE = Path(__file__).resolve().parent / "state.json"

def save_state(quizzes, high_score):
    data = {
        "high_score": high_score,
        "quizzes": []
        }

    for quiz in quizzes:
        data["quizzes"].append({
            "question": quiz.question,
            "options": quiz.options,
            "answer": quiz.answer,
            "explanation": quiz.explanation
            })

    with open(STATE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_state():
    if not STATE_FILE.exists():
        return None

    with open(STATE_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    quizzes = []

    for item in data["quizzes"]:
        quiz = Quiz(
            item["question"],
            item["options"],
            item["answer"],
            item["explanation"]
            )
        quizzes.append(quiz)

    return quizzes, data["high_score"]
