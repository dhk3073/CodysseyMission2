from quiz import Quiz

quizzes = [
    Quiz(
        "다음 변수의 자료형은 무엇인가? a = '10' ",
        ["int", "str", "float", "dict"],
        2,
        "str은 문자열로, ''로 덮어 표기한다."
    ),
    Quiz(
        "순환 가능한 객체를 사용하여 표현하는 반복문은?",
        ["while", "if", "for", "switch"],
        3,
        "for문은 반복 가능한 객체를 순회, while문은 조건식이 참인 동안 반복된다."
    ),
    Quiz(
        "반복문을 즉시 종료하는 키워드는?",
        ["continue", "break", "pass", "return"],
        2,
        "break는 가장 안쪽의 반복문을 종료한다."
    ),
    Quiz(
        "조건식이 참일 때 수행되는 조건문이 아닌 것은?",
        ["elif", "if", "else", "bool"],
        3,
        "else는 if문에 부합하지 않는 조건일때 실행된다."
    ),
    Quiz(
        "키와 값으로 데이터를 저장하는 자료형은?",
        ["list", "tuple", "set", "dict"],
        4,
        "dict는 키와 값의 쌍으로 데이터를 저장한다."
    ),
    Quiz(
        "다음 중 메서드에 해당하는 함수는 무엇인가?",
        ["list()", "print()", "set()", ".split()"],
        4,
        "메서드는 객체 뒤에 .{메서드명}() 형식으로 붙여 사용한다."
    ),
    Quiz(
        "클래스의 생성자를 뜻하는 함수는?",
        ["__init__", "__eq__", "__del__", "def"],
        1,
        "__eq__ 는 '=' 에 대한 연산자 오버라이딩, __del__은 소멸자, def는 함수 선언 명령어이다. "
    )
]

def add_quiz(quiz):
    quizzes.append(quiz)

def get_quizzes():
    return quizzes


