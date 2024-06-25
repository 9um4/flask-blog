from flask import Flask

def create_app():
    app = Flask(__name__)

    # 블루프린트 등록
    # 라우팅 관련 설정
    from .main.routes import main
    app.register_blueprint(main)

    return app