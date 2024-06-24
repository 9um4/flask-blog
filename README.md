## Chapter 01: Flask 초기 설정
Flask는 Python으로 작성된 경량 웹 프레임워크로, 간단한 웹 애플리케이션을 빠르게 개발할 수 있도록 도와줍니다. 다음은 Flask를 기반으로 간단한 웹사이트를 만드는 것에 대한 설명입니다.

### 1. Python과 pip 설치
먼저, Python과 pip가 설치되어 있는지 확인합니다.

```bash
python --version
pip --version
```

Python과 pip이 설치되지 않았다면, Python의 [공식 웹사이트](https://www.python.org/downloads/)에서 설치할 수 있습니다.

### 2. 가상 환경 설정
가상 환경을 생성하고 활성화합니다. 가상 환경은 프로젝트별로 패키지를 관리할 수 있게 해줍니다.

```bash
python -m venv .venv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate  # PowerShell
```

### 3. Flask 설치
가상 환경을 활성화한 후 Flask를 설치합니다.

```bash
pip install Flask
```

### 4. 기본 Flask 애플리케이션 생성
새 디렉토리를 만들고 그 안에 `app.py` 파일을 생성합니다.

```bash
mkdir myflaskapp
cd myflaskapp
touch app.py  # Linux/Mac
new-item app.py  # Windows PowerShell
```

`app.py` 파일에 다음 코드를 작성합니다:

```python
from flask import Flask

app = Flask(__name__)

# URL을 특정하기 위한 decorator
@app.route('/')
# 함수 이름은 상관 없음
def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

### 5. Flask 애플리케이션 실행
Flask 애플리케이션을 실행합니다.

```bash
python app.py
```

브라우저에서 `http://127.0.0.1:5000/`를 방문하면 "Hello, Flask!" 메시지를 볼 수 있습니다.

### 6. 환경 변수 설정 (선택 사항)
개발 시 Flask의 환경 변수를 설정하여 디버그 모드를 활성화할 수 있습니다. `.flaskenv` 파일을 생성하고 다음 내용을 추가합니다:

환경 변수 파일은 프로젝트의 root 폴더에 생성해야 합니다.

```bash
FLASK_APP=app.py
FLASK_ENV=development
```

경우에 따라서 `python-dotenv`를 요구하는 경우가 있습니다. 그럴 경우 pip를 이용해 설치합니다.

```bash
pip install python-dotenv
```

이제 Flask를 실행할 때 간단히 `flask run` 명령어를 사용할 수 있습니다.

```bash
flask run
```

이제 Flask 초기 설정이 완료되었습니다. 필요한 경우, 추가적인 패키지 설치나 설정을 진행하면 됩니다.