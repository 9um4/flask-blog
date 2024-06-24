## Chapter 02: html 파일을 사용하기
Flask에서 HTML 파일을 반환하려면 `render_template` 함수를 사용합니다. 이를 위해 몇 가지 단계를 따라야 합니다:

### 1. **템플릿 디렉토리 생성**:
   Flask는 기본적으로 `templates` 디렉토리에서 HTML 파일을 찾습니다. 프로젝트 루트 디렉토리에 `templates` 디렉토리를 생성합니다.

   ```bash
   mkdir templates
   ```

### 2. **HTML 파일 생성**:
   `templates` 디렉토리에 HTML 파일을 생성합니다. 예를 들어, `index.html` 파일을 생성합니다.

   ```bash
   touch templates/index.html  # Linux/Mac
   type nul > templates/index.html  # Windows
   ```

   `index.html` 파일에 간단한 HTML 내용을 작성합니다.

   ```html
   <!-- templates/index.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Hello, Flask!</title>
   </head>
   <body>
       <h1>Hello, Flask with HTML!</h1>
   </body>
   </html>
   ```

### 3. **Flask 애플리케이션에서 HTML 파일 반환**:
   `render_template` 함수를 사용하여 HTML 파일을 반환하도록 `app.py` 파일을 수정합니다.

   ```python
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       return render_template('index.html')

   if __name__ == '__main__':
       app.run(debug=True)
   ```

이제 Flask 애플리케이션을 실행하면, 루트 경로(`/`)에 접속할 때 `index.html` 파일이 반환됩니다.

```bash
flask run
```

브라우저에서 `http://127.0.0.1:5000/`를 방문하면 "Hello, Flask with HTML!" 메시지가 있는 HTML 페이지를 볼 수 있습니다.

### 요약
1. 프로젝트 루트 디렉토리에 `templates` 디렉토리를 생성합니다.
2. `templates` 디렉토리에 HTML 파일을 생성합니다.
3. Flask 애플리케이션에서 `render_template` 함수를 사용하여 HTML 파일을 반환합니다.

이 방법으로 HTML 파일을 반환할 수 있습니다. 추가로, 템플릿 내에서 변수 사용이나 다른 템플릿 기능을 사용할 수도 있습니다.