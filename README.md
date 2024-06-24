## Chapter 03: 동적으로 웹 페이지의 값을 결정하기
Flask에서 동적으로 값을 결정하여 HTML 파일에 전달하는 방법은 `render_template` 함수와 Jinja2 템플릿 엔진을 사용하는 것입니다. Jinja2는 Flask의 기본 템플릿 엔진으로, HTML 파일에서 동적으로 값을 삽입할 수 있게 해줍니다.

다음은 동적으로 값을 결정하여 HTML의 값을 변경하는 예제입니다.

### 1. HTML 파일 수정
먼저 `index.html` 파일을 수정하여 동적으로 값을 받을 수 있도록 합니다. 예를 들어, `title`과 `message` 값을 동적으로 받아서 표시하도록 합니다.

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ message }}</h1>
</body>
</html>
```

### 2-1. 매개변수를 이용한 값의 전달
`app.py` 파일에서 동적으로 값을 결정하고 이를 HTML 템플릿에 전달하도록 수정합니다.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 동적으로 값을 결정
    title = "Hello, Dynamic Flask!"
    message = "This is a dynamic message passed to the template."
    
    # render_template 함수로 값을 전달
    return render_template('index.html', title=title, message=message)

if __name__ == '__main__':
    app.run(debug=True)
```

### 2-2. 딕셔너리 자료형을 이용한 값의 전달
일일이 매개변수를 지정해 줄 필요 없이 아래와 같이 딕셔너리 자료형을 이용해 html 템플릿에 전달할 수 있습니다.
```py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 동적으로 값을 결정
    context = {
        'title': "Hello, Dynamic Flask!",
        'message': "This is a dynamic message passed to the template."
    }
    
    # render_template 함수로 딕셔너리를 전달
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
```

### 3. Flask 애플리케이션 실행
Flask 애플리케이션을 실행하고 브라우저에서 확인합니다.

```bash
flask run
```

브라우저에서 `http://127.0.0.1:5000/`를 방문하면, 동적으로 설정된 `title`과 `message` 값이 HTML 페이지에 표시됩니다.

### 요약
1. **HTML 파일 수정**: 템플릿 변수(`{{ 변수명 }}`)를 사용하여 동적 값을 받을 수 있도록 HTML 파일을 수정합니다.
2. **Flask 애플리케이션 수정**: `render_template` 함수에 전달할 변수를 설정하고, 이를 템플릿으로 전달합니다.

이 방법을 사용하면 Flask에서 동적으로 값을 결정하여 HTML 파일에 반영할 수 있습니다. Jinja2 템플릿 엔진을 사용하면 조건문, 반복문 등을 통해 더욱 복잡한 동적 콘텐츠도 쉽게 생성할 수 있습니다.