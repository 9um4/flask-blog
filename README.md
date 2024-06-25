## Chapter 06: app.py의 모듈화
우리가 html 파일들을 모듈화 했던 것처럼 python 프로젝트 또한 모듈화가 가능합니다. 이번 챕터에서는 그 방법에 대해서 이야기를 나누어 보도록 하겠습니다.

Flask의 블루프린트(Blueprint)는 대규모 애플리케이션을 구성하고 관리하기 위한 강력한 방법입니다. 블루프린트는 Flask 애플리케이션의 다양한 구성 요소(예: 라우트, 뷰 함수, 템플릿, 정적 파일 등)를 모듈화하고 조직화할 수 있는 방법을 제공합니다. 이를 통해 코드의 가독성과 유지보수성을 향상시키고, 팀 간의 협업을 용이하게 합니다.

### 블루프린트의 주요 특징
1. **모듈화**: 블루프린트를 사용하면 애플리케이션의 기능을 독립적인 모듈로 나눌 수 있습니다.
2. **재사용성**: 블루프린트는 여러 애플리케이션에서 재사용할 수 있습니다.
3. **조직화**: 관련된 라우트, 뷰 함수, 템플릿 등을 하나의 블루프린트로 그룹화하여 관리할 수 있습니다.

### 예제: 블루프린트를 사용한 Flask 애플리케이션

#### 1. 프로젝트 디렉토리 구조
먼저, Flask 애플리케이션의 디렉토리 구조를 설정합니다.

```
root/
├── backend/
│   ├── templates/
│   │   ├── components/
│   │   │   ├── header.html
│   │   │   └── footer.html
│   │   ├── pages/
│   │   │   ├── index.html
│   │   │   └── about.html
│   │   ├── base.html
│   ├── __init__.py
│   └── main/
│       ├── __init__.py
│       └── routes.py
└── run.py
```

#### 2. `main/__init__.py` 파일 생성
`backend/main/__init__.py` 파일을 생성하여 등록할 블루프린트를 선언하고 초기화합니다.

```python
from flask import Blueprint

main = Blueprint('main', __name__)
```

#### 3. `main/routes.py` 파일 생성 및 라우팅 진행
`myflaskapp/main/routes.py` 파일을 생성하여 `main` 블루프린트의 라우트를 정의합니다.

```python
# myflaskapp/main/routes.py
from flask import render_template
from . import main

@main.route('/')
def home():
    return render_template('pages/index.html')

@main.route('/about')
def about():
    return render_template('pages/about.html')
```

#### 4. `__init__.py` 파일 생성

앞서 선언한 블루프린트를 import하여 블루프린트를 등록합니다.

```python
# myflaskapp/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # 블루프린트 등록
    from .main.routes import main
    app.register_blueprint(main)

    return app
```

#### 4. `run.py` 파일 생성
최상위 디렉토리에 `run.py` 파일을 생성하여 애플리케이션을 실행할 진입점을 만들어 줍니다.

```python
# run.py
from myflaskapp import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

#### 5. `.flaskenv` 파일 변경
프로젝트의 root 폴더에 `.flaskenv` 파일을 옮기고 프로젝트의 구조에 맞추어 환경 변수를 변경합니다.

```py
FLASK_APP=backend       # 프로젝트 폴더 이름
FLASK_ENV=development   # 개발중일 경우 development로 설정 
```

#### 6. 실행
아래 둘 중 하나의 명령어를 프로젝트의 root 폴더에 입력하여 실행할 수 있습니다.

```bash
python run.py
```

```bash
flask run
```

### 블루프린트의 사용 방법
1. **블루프린트 정의**: `Blueprint` 클래스를 사용하여 블루프린트를 정의합니다.
2. **라우트 등록**: 블루프린트에 라우트를 등록합니다.
3. **애플리케이션에 블루프린트 등록**: `Flask` 애플리케이션 객체에 `register_blueprint` 메서드를 사용하여 블루프린트를 등록합니다.
    > 이 때, 블루프린트를 등록할 때에는 라우팅을 진행한 파일에서 import를 진행해 등록합니다.

### 요약
- 블루프린트는 Flask 애플리케이션을 모듈화하고 조직화하는 데 사용됩니다.
- 블루프린트를 사용하면 애플리케이션의 구성 요소를 독립적으로 관리할 수 있습니다.
- 블루프린트를 정의하고, 라우트를 등록한 후, 애플리케이션에 블루프린트를 등록하여 사용합니다.

이 방법을 통해 Flask 애플리케이션의 구조를 개선하고 코드의 가독성과 유지보수성을 높일 수 있습니다.