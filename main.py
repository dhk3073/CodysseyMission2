from quiz import *
import quiz_data

def main():
        print("Codyssey Quiz Game")
        high_score = 0
        game = QuizGame(quiz_data.quizzes)

        while True:
            show_menu()
            choice = get_num("select Menu : ", 1, 5)

            if choice == 1:
                print("==== 퀴즈 풀기(미구현) ====")
                game.start_game()
                
                for quiz in game.quizzes:
                        quiz.display()
                        answer = get_num("input answer : ", 1, 4)
                        
                        if game.submit_answer(quiz,answer):
                                print("correct!")
                        else:
                                print("wrong...")
                                
                        print(f"해설 : {quiz.explanation}")
                        print()
                        
                if game.score > high_score:
                        high_score = game.score
                        print("New Record!")

                game.show_result()
                
            elif choice == 2:
                print("==== 퀴즈 추가 ====")
                create_quiz()
            elif choice == 3:
                print("==== 퀴즈 목록 ====")
                show_quiz_list()
            elif choice == 4:
                print("==== 최고 점수 ====")
                print(f"High Score : {high_score}")
            elif choice == 5:
                print("==== 게임 종료 ====")
                break


            
def show_menu():
        print("==== Menu ====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수")
        print("5. 종료")      

def get_num(prompt, min_val, max_val):
        while True:
                raw = input(prompt).strip()

                try:
                        num = int(raw)
                except ValueError:
                        print("wrong input(only Num)")
                        continue

                if min_val <= num <= max_val:
                        return num
                else:
                        print(f"wrong input({min_val} ~ {max_val})")

def get_text(prompt):
        while True:
                text = input(prompt)

                if text.strip():
                        return text

                print("Can not input empty text.")

def create_quiz():
        question = get_text("문제를 입력하세요: ")
        options = []

        for i in range(4):
                option = get_text(f"{i+1}번 보기: ")
                options.append(option)

        answer = get_num("정답 번호 : ", 1, 4)
        
        explanation = get_text("정답 해설 : ")

        new_quiz = Quiz(question, options, answer, explanation)

        quiz_data.add_quiz(new_quiz)

        print("success add quiz")

def show_quiz_list():
        quizzes = quiz_data.get_quizzes()

        if not quizzes:
                print("no quizzes")
                return

        for i, quiz in enumerate(quizzes, 1):
                print(f"[Q {i}]")
                quiz.display()


if __name__ == "__main__":
	main()
