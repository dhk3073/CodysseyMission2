# 프로젝트 개요

Python 3.10 이상을 사용한 콘솔 기반 퀴즈게임

# 파일 구조

QuizGame/
├── main.py          # 메뉴 출력 및 사용자 입력 처리
├── quiz.py          # Quiz 클래스 정의
├── quiz_game.py     # QuizGame 클래스 및 게임 진행
├── quiz_data.py     # 퀴즈 데이터 관리
├── storage.py       # JSON 파일 저장 및 불러오기
├── state.json       # 퀴즈 데이터 및 최고 점수 저장
└── README.md        # 프로젝트 설명 및 실행 방법

# state.json 파일 스키마

state.json은 프로젝트 최상위 디렉터리에 생성되며, 퀴즈 데이터와 최고 점수를 저장하는 파일입니다.

저장 형식: JSON

문자 인코딩: UTF-8

저장 내용: 최고 점수, 문제, 선택지, 정답 번호, 해설

데이터 구조 예시

{
    "high_score": 3,
    "quizzes": [
        {
            "question": "Python에서 출력에 사용하는 함수는?",
            "options": ["input", "print", "int", "str"],
            "answer": 2,
            "explanation": "print()는 값을 출력하는 함수입니다."
        }
    ]
}

high_score는 최고 점수를 저장하며, quizzes는 퀴즈 객체들의 데이터를 목록으로 저장합니다.

프로그램은 storage.py를 통해 데이터를 저장하고 불러옵니다. 저장 파일이 없는 경우 기본 데이터로 시작하도록 설계했습니다.


# 퀴즈 주제와 선정 이유

* 코드 사용 중 이용한 Python 명령어나 개념 위주로 출제
* 저번 시험의 경향을 보아 명령어 위주의 테스트가 이루어질 것이라 예상함

# 실행 방법

* 다음 프로그램을 미리 설치해 주세요.



\- \[Python 3.10 이상](https://www.python.org/downloads/)

\- \[Git](https://git-scm.com/downloads/win)



* 퀴즈 게임 다운로드



Windows 시작 메뉴에서 \*\*PowerShell\*\*을 검색해 실행합니다.



아래 명령어를 한 줄씩 입력하고 Enter를 누릅니다.



```powershell

cd "$HOME\\Desktop"

git clone <GitHub 저장소 주소> QuizGame

cd QuizGame

```



`<GitHub 저장소 주소>`는 이 프로젝트의 GitHub 주소로 바꿔 입력해 주세요.



* 퀴즈 게임 실행



다음 명령어를 입력합니다.



```powershell

python main.py

```



메뉴가 나타나면 숫자를 입력해 게임을 이용할 수 있습니다.



* 재실행하기



PowerShell을 열고 다음 명령어를 입력합니다.



```powershell

cd "$HOME\\Desktop\\QuizGame"

python main.py

```



* 저장 경로에 유의하세요



* 최신 버전으로 업데이트하기



GitHub에 새로운 변경사항이 등록되었다면 다음 명령어로 업데이트할 수 있습니다.



```powershell

cd "$HOME\\Desktop\\QuizGame"

git pull

python main.py

```



참고: 게임에서 저장한 퀴즈와 최고 점수는 `state.json` 파일에 보관됩니다. 프로젝트 폴더를 삭제하면 저장 데이터도 함께 사라질 수 있습니다.

## 주요 기능

* 메뉴
* 종료 기능 \[o]
* 선택 기능 \[o]
* 오입력 처리 \[o]
* 퀴즈 풀기 \[o]
* 퀴즈 출제 \[o]
* 정답 입력 \[o]
* 정/오답 여부 출력 \[o]
* 결과 출력 \[o]
* 예외사항 처리 \[o]
* 퀴즈 추가 \[o]
* 필요한 정보 : 문제, 선택지(4개), 정답 번호 \[o]
* 오입력 처리 \[o]
* 추가 퀴즈 저장 \[o]
* 퀴즈 목록 확인 \[o]
* 저장 퀴즈 목록 확인 \[o]
* 예외사항 처리 \[o]
* 점수 확인 \[o]
* 최고 점수 확인 \[o]
* 퀴즈 종료 시 최고 점수와 비교 및 갱신 \[o]
* 최고 점수 저장 \[o]
* JSON 파일을 통한 데이터 저장 \[o]



## 실행 환경

* Python 3.10 이상
* Python 표준 라이브러리

## 저장소 복제 실습

* 이 줄은 저장소 복제 및 커밋 반영여부를 확인하기 위해 작성되었습니다.