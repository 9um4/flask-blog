## Chapter 04: 템플릿의 상속을 바탕으로 한 모듈화 (1)
Flask와 Jinja2 템플릿 엔진을 사용하여 공통 요소(예: 헤더, 푸터 등)를 별도의 템플릿 파일에 저장하고 이를 포함하는 방식으로 웹 페이지를 구현할 수 있습니다. 이를 위해 Jinja2의 템플릿 상속 및 포함 기능을 사용할 수 있습니다.

### 예제: 공통 헤더와 푸터 포함하기

#### 1. 프로젝트 디렉토리 구조
먼저 프로젝트 디렉토리를 구성합니다:

```
myflaskapp/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
└── app.py
```

#### 2. `base.html` 파일 생성
공통 요소를 포함할 기본 템플릿 파일 `base.html`을 생성합니다:

> `{% block <블록 이름> %} {% endblock %}`으로 감싸져 있는 부분이 추후 상속할 템플릿에서 대체될 내용입니다. 해당 내용이 존재하지 않을 경우 상속된 템플릿에 적혀있는 내용을 우선으로 표시됩니다.

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Default Title{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Website Header</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
            </ul>
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>My Website Footer</p>
    </footer>
</body>
</html>
```

#### 3. `index.html` 파일 생성
홈 페이지 템플릿 파일 `index.html`을 생성하고 `base.html`을 상속합니다:

```html
<!-- templates/index.html -->
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
<h2>Welcome to the Home Page</h2>
<p>This is the home page content.</p>
{% endblock %}
```

#### 4. `about.html` 파일 생성
소개 페이지 템플릿 파일 `about.html`을 생성하고 `base.html`을 상속합니다:

```html
<!-- templates/about.html -->
{% extends 'base.html' %}

{% block title %}About{% endblock %}

{% block content %}
<h2>About Us</h2>
<p>This is the about page content.</p>
{% endblock %}
```

#### 5. `app.py` 파일 수정
Flask 애플리케이션을 수정하여 라우트와 템플릿을 연결합니다:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### 요약
1. **기본 템플릿 생성**: 공통 요소(헤더, 푸터 등)를 포함하는 `base.html` 파일을 생성합니다.
2. **페이지별 템플릿 생성**: 개별 페이지 템플릿(`index.html`, `about.html` 등)을 생성하고 `base.html`을 상속합니다.
3. **Flask 애플리케이션 수정**: 라우트와 템플릿을 연결하여 각 페이지를 렌더링합니다.

이 방법을 사용하면 공통 요소를 한 곳에서 관리할 수 있어 유지보수가 쉬워지고, 템플릿 상속을 통해 재사용성을 높일 수 있습니다.