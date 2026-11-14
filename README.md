# 프로젝트 개요

Python 3.10 이상을 사용한 콘솔 기반 퀴즈게임

# 커밋 규칙
* `feat` : 기능 추가
* `chore` : 프로젝트 설정 및 관리
* `merge` : 브랜치 및 작업 내용 병합
* `docs` : 텍스트 작업

# 파일 구조
```bash
QuizGame/
├── main.py          # 메뉴 출력 및 사용자 입력 처리
├── quiz.py          # Quiz 클래스 정의
├── quiz_game.py     # QuizGame 클래스 및 게임 진행
├── quiz_data.py     # 퀴즈 데이터 관리
├── storage.py       # JSON 파일 저장 및 불러오기
├── state.json       # 퀴즈 데이터 및 최고 점수 저장
└── README.md        # 프로젝트 설명 및 실행 방법
```

# 파일별 주요 기능 및 관련 속성/메서드 (수정 시 ctrl+f 로 탐색 권장)

## 1. 파일별 역할
```
| 파일 | 담당 기능 |
|---|---|
| `main.py` | 메뉴, 사용자 입출력 및 실행 흐름 |
| `quiz.py` | 퀴즈 객체, 정답 판정 및 점수 관리 |
| `quiz_data.py` | 기본 퀴즈 데이터 및 목록 관리 |
| `storage.py` | JSON 데이터 저장 및 복원 및 백업·초기화 |
```
## 2. 요구사항 변경별 영향 매핑
```
| 요구사항 변경 | 영향받는 파일 | 관련 함수·메서드 및 변수 |
|---|---|---|
| 메뉴 구성 변경 | `main.py` | `main()`, `show_menu()` |
| 입력 검증 방식 변경 | `main.py` | `get_num()`, `get_text()` |
| 퀴즈 보기 개수 변경 | `main.py`, `quiz_data.py` | `main()`, `create_quiz()`, `quizzes` |
| 퀴즈 출력 형식 변경 | `quiz.py`, `main.py` | `Quiz.display()`, `show_quiz_list()` |
| 정답 판정 방식 변경 | `quiz.py`, `main.py` | `Quiz.check_answer()`, `QuizGame.submit_answer()`, `main()` |
| 점수 계산 방식 변경 | `quiz.py`, `main.py` | `QuizGame.submit_answer()`, `QuizGame.show_result()`, `main()` |
| 퀴즈 속성 추가·변경 | 전체 파일 | `Quiz.__init__()`, `create_quiz()`, `quizzes`, `save_state()`, `load_state()` |
| 퀴즈 추가 방식 변경 | `main.py`, `quiz_data.py` | `create_quiz()`, `add_quiz()` |
| 퀴즈 수정·삭제 기능 추가 | `main.py`, `quiz_data.py` | `main()`, `show_menu()`, 신규 함수 구현 필요 |
| 최고점수 관리 방식 변경 | `main.py`, `storage.py` | `main()`, `save_state()`, `load_state()` |
| 저장 파일 경로 변경 | `storage.py` | `STATE_FILE` |
| JSON 데이터 구조 변경 | `storage.py`, `main.py` | `save_state()`, `load_state()`, `main()` |
| 게임 결과 출력 변경 | `quiz.py` | `QuizGame.show_result()` |
| 데이터 복구 기능 | `storage.py` | `restore_state(), BACKUP_FILE` |
| 데이터 초기화 기능 | `storage.py` | `reset_state(), STATE_FILE` |
| 게임 결과 출력 변경 | `storage.py` | `reset_state(), STATE_FILE` |
```

※ 위 매핑은 현재 구현을 기준으로 작성했으며, 실제 수정 범위는 세부 요구사항에 따라 달라질 수 있습니다.

# state.json 파일 스키마

state.json은 프로젝트 최상위 디렉터리에 생성되며, 퀴즈 데이터와 최고 점수를 저장하는 파일입니다.

저장 형식: JSON

문자 인코딩: UTF-8

저장 내용: 최고 점수, 문제, 선택지, 정답 번호, 해설

데이터 구조 예시
```bash
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
```
high_score는 최고 점수를 저장하며, quizzes는 퀴즈 객체들의 데이터를 목록으로 저장합니다.

프로그램은 storage.py를 통해 데이터를 저장하고 불러옵니다. 저장 파일이 없는 경우 기본 데이터로 시작하도록 설계했습니다.

# JSON 저장 방식의 한계

* 성능 측면
	* JSON 텍스트를 PYTHON 데이터화해야 하거나 그 역을 작업하기 때문에, 데이터가 많을 수록 속도가 저하됨
	* 일부 데이터 수정을 하더라도 전체 파일을 다시 저장해야함

* 메모리 측면
	* 파일 전체를 읽어오기 때문에 대용량 파일의 경우 메모리 사용량이 증가함

# 객체지향 채택 사유

* 유지 보수 및 기능 추가/삭제의 용이성을 위해 각 함수및 변수를 클래스에 종속시켰습니다.
* 객체지향 프로그래밍을 구현함으로 기능에 대한 수정 필요 시 전체 코드가 아닌 클래스에서 대응하는 메서드 및 속성을 수정하는것으로 기능 수정이 가능합니다.


# 퀴즈 주제와 선정 이유

* 코드 사용 중 이용한 Python 명령어나 개념 위주로 출제
* 저번 시험의 경향을 보아 명령어 위주의 테스트가 이루어질 것이라 예상함

# 실행 방법(CLI 기준)

* 다음 프로그램을 미리 설치해 주세요.



\- \[Python 3.10 이상](https://www.python.org/downloads/)

\- \[Git](https://git-scm.com/downloads/win)



* 퀴즈 게임 다운로드



Windows 시작 메뉴에서 PowerShell을 검색해 실행합니다.



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

* 이 줄은 저장소 복제 및 커밋 반영여부를 확인하기 위해 작성되었으며, 정상작동여부를 확인했습니다.

## Git 브랜치 전환 실습

main - feature/quiz-class 브랜치 이동을 통해 연습

* 병합 시기 : quiz.py quiz_data.py 파일의 구성 완료 후
* 브랜치 - 병합 목적 : 기능 추가로 인해 main.py 파일이 의도치 않은 오작동을 하는 것을 피하기 위해 별도 브랜치에서 개발 후 정상작동을 확인 한 뒤 merge

```bash
git checkout feature/quiz-class
git branch

git checkout main
git branch

git reflog -4
```

로그상에 정상출력됨을 확인
