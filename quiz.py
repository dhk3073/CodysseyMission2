class Quiz:
        def __init__(self, question, options, answer, explanation):
                self.question = question
                self.options = options
                self.answer = answer
                self.explanation = explanation

        def display(self):
                print("==============================")
                print(f"Q : {self.question}")

                for i, option in enumerate(self.options, start=1):
                        print(f"{i}.{option}")

        def check_answer(self, choice):
                return choice == self.answer

class QuizGame:
        def __init__(self, quizzes):
                self.quizzes = quizzes
                self.score = 0

        def start_game(self):
                self.score = 0

        def submit_answer(self, quiz, choice):
                if quiz.check_answer(choice):
                        self.score += 1
                        return True
                return False

        def show_result(self):
                total = len(self.quizzes)
                print("==== 퀴즈 결과 ====")
                print(f"정답: {self.score} / {total}")
