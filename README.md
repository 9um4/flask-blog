## Chapter 05: 템플릿의 상속을 바탕으로 한 모듈화 (2)
Jinja2 템플릿 엔진을 사용하여 `header.html`과 `footer.html` 같은 파일을 만들어 공통 요소를 분리하고, 이를 각 페이지 템플릿에서 포함할 수 있습니다. 이를 위해 Jinja2의 `{% include %}` 태그를 사용합니다.

### 예제: 헤더와 푸터를 별도의 파일로 분리하여 포함하기

#### 1. 프로젝트 디렉토리 구조
프로젝트 디렉토리를 다음과 같이 구성합니다:

```
myflaskapp/
├── templates/
│   ├── header.html
│   ├── footer.html
│   ├── base.html
│   ├── index.html
│   ├── about.html
└── app.py
```

#### 2. `header.html` 파일 생성
공통 헤더 내용을 포함하는 `header.html` 파일을 생성합니다:

```html
<!-- templates/header.html -->
<header>
    <h1>My Website Header</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
        </ul>
    </nav>
</header>
```

#### 3. `footer.html` 파일 생성
공통 푸터 내용을 포함하는 `footer.html` 파일을 생성합니다:

```html
<!-- templates/footer.html -->
<footer>
    <p>My Website Footer</p>
</footer>
```

#### 4. `base.html` 파일 수정
기본 템플릿 파일 `base.html`을 수정하여 `header.html`과 `footer.html` 파일을 포함합니다:

> `{% include '<파일 경로>' %}`는 해당 html 파일의 내용을 직접적으로 참조합니다. 파일 경로는 해당 구문을 작성하는 파일을 기준으로 상대 경로를 입력합니다.

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
    {% include 'header.html' %}

    <main>
        {% block content %}{% endblock %}
    </main>

    {% include 'footer.html' %}
</body>
</html>
```

#### 5. `index.html` 파일 생성
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

#### 6. `about.html` 파일 생성
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

#### 7. `app.py` 파일 수정
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
1. **공통 요소 파일 생성**: `header.html`과 `footer.html` 파일을 생성하여 공통 요소를 포함합니다.
2. **기본 템플릿 수정**: `base.html` 파일에서 `{% include %}` 태그를 사용하여 공통 요소 파일을 포함합니다.
3. **페이지별 템플릿 생성 및 수정**: 각 페이지 템플릿에서 `base.html`을 상속받아 개별 콘텐츠를 정의합니다.
4. **Flask 애플리케이션 수정**: 라우트와 템플릿을 연결합니다.

이 방법을 사용하면 공통 요소를 별도의 파일로 분리하여 관리할 수 있어 유지보수가 쉬워지고, 템플릿의 재사용성을 높일 수 있습니다.