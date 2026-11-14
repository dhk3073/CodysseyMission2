from storage import backup_state, restore_state
from quiz import *
from storage import *
import quiz_data

## 메인 함수(사용자 입력 및 메뉴 출력)
def main():

        print("Codyssey Quiz Game")
        high_score = 0
        game = QuizGame(quiz_data.quizzes)
        saved = load_state()

        if saved is not None:
                quizzes, high_score = saved
                quiz_data.quizzes = quizzes

        game = QuizGame(quiz_data.get_quizzes())
        ## EOF, 인터럽트 대비용 try-except
        try:
                while True:
                    show_menu()
                    choice = get_num("select Menu : ", 1, 8)

                    if choice == 1:
                        print("==== 퀴즈 풀기 ====")
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
                                save_state(quiz_data.get_quizzes(), high_score)

                        game.show_result()
                        
                    elif choice == 2:
                        print("==== 퀴즈 추가 ====")
                        create_quiz()
                        save_state(quiz_data.get_quizzes(), high_score)
                    elif choice == 3:
                        print("==== 퀴즈 목록 ====")
                        show_quiz_list()
                    elif choice == 4:
                        print("==== 최고 점수 ====")
                        print(f"High Score : {high_score}")
                    elif choice == 5:
                        print("==== 게임 종료 ====")
                        ## 저장 절차 : 데이터 저장 실패, 입력처리 실패 대비 재입력 요구                        
                        while True:
                                if save_state(quiz_data.get_quizzes(), high_score):
                                        return
                                
                                print("저장 실패")
                                
                                retry = input("다시 저장하시겠습니까? (y/n): ").strip().lower()

                                if retry == 'y':
                                        continue
                                elif retry == 'n':
                                        print("저장되지 않은 데이터가 있을 수 있습니다.")
                                        return
                                else:
                                        print("잘못된 입력입니다.")
                    elif choice == 6:
                        print("데이터 백업")
                        try:
                            backup_state()
                        except:
                            ("백업 실패")
                    elif choice == 7:
                        print("데이터 복구")
                        try:
                            restore_state()
                        except:
                            ("복구 실패")
                    elif choice == 8:
                        print("데이터 초기화")
                        try:
                            reset_state()
                            print("초기화 완료. 프로그램을 재실행하세요.")
                            return
                            
                        except:
                            ("초기화 실패")
                        
        ## EOF, 인터럽트 감지 시 작동                                        
        except (KeyboardInterrupt, EOFError):
                print("\n입력이 중단되었습니다. 데이터를 저장합니다.")

                if save_state(quiz_data.get_quizzes(), high_score):
                    print("안전하게 종료합니다.")
                else:
                    print("저장에 실패했습니다. 일부 데이터가 유실될 수 있습니다.")

## 메뉴 출력 함수            
def show_menu():
        print("==== Menu ====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수")
        print("5. 종료")
        print("6. 데이터 백업")
        print("7. 데이터 복구")
        print("8. 데이터 초기화")

## 입력값 검사(숫자)
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
##입력값 검사(문자)
def get_text(prompt):
        while True:
                text = input(prompt)

                if text.strip():
                        return text

                print("Can not input empty text.")

##퀴즈 추가
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

##퀴즈 목록 출력
def show_quiz_list():
        quizzes = quiz_data.get_quizzes()

        if not quizzes:
                print("no quizzes")
                return

        for i, quiz in enumerate(quizzes, 1):
                print(f"[Q {i}]")
                quiz.display()

##메인 함수 검사
if __name__ == "__main__":
	main()
