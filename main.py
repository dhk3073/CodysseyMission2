def main():
        print("Codyssey Quiz Game")
        show_menu()

        while True:
            
            choice = get_num("select Menu : ", 1, 5)

            if choice == 1:
                print("==== 퀴즈 풀기(미구현) ====")
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
