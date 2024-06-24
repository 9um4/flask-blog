from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    title: str = "Hello, Flask with HTML!"
    message: str = "This is my first Flask app with HTML!"
    return render_template('index.html', title=title, message=message)

    """
    매개변수를 지정해 주는 것 대신 dictionary를 사용할 수 있음
    
    context = {
        'title': 'Hello, Flask with HTML!',
        'message': 'This is my first Flask app with HTML!'
    }
    return render_template('index.html', **context)
    """

if __name__ == "__main__":
    app.run(debug=True)