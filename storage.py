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
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    except OSError as error:
        print("파일 저장 오류: {error}")
        return False

    print("데이터 저장 완료")
    return True

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

    except FileNotFoundError:
        print("저장 파일이 없습니다. 기본 데이터로 시작합니다.")
        return None

    except (json.JSONDecodeError, UnicodeDecodeError):
        print("저장 파일이 손상되었습니다.")
        return None
    
    except (KeyError, TypeError, ValueError):
        print("저장 파일이 올바르지 않습니다.")
        return None

    except OSError as error:
        print(f"파일 읽기 오류: {error}")
        return None
