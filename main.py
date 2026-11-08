from quiz_data import quizzes
from quiz import QuizGame

def main():
        print("Codyssey Quiz Game")
        game = QuizGame(quizzes)

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

                game.show_result()
            elif choice == 2:
                print("==== 퀴즈 추가(미구현) ====")
            elif choice == 3:
                print("==== 퀴즈 목록(미구현) ====")
            elif choice == 4:
                print("==== 최고 점수(미구현) ====")
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


if __name__ == "__main__":
	main()
