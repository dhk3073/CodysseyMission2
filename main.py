def main():
	print("Codyssey Quiz Game")
        show_menu()

        while True:
            
            choice = input("select Menu(1~5) : ").strip()

            if choice == "1":
                print("==== 퀴즈 풀기(미구현) ====")
            elif choice == "2":
                print("==== 퀴즈 추가(미구현) ====")
            elif choice == "3":
                print("==== 퀴즈 목록(미구현) ====")
            elif choice == "4":
                print("==== 최고 점수(미구현) ====")
            elif choice == "5":
                print("==== 게임 종료 ====")
                break
            else:
                print("wrong menu(1~5)")  
            
def show_menu():
        print("==== Menu ====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수")
        print("5. 종료")      


if __name__ == "__main__":
	main()
