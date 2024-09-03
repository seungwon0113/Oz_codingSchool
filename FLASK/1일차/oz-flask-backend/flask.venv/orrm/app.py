from flask import Flask, render_template
from flask_smorest import Api
from db import db
from models import User, Board
from routes.board import board_blp
from routes.user import user_blp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:seungwon0113@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 메모리 영역에서 객체가 바뀔 때 마다 트래킹 하는 것 : 메모리 과부하로 인해 False

# 앱 객체 전달
db.init_app(app)

# bluepring 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
# board_blp 등록
api.register_blueprint(board_blp)
api.register_blueprint(user_blp)


@app.route('/manage-boards')
def manage_boards():
    return render_template('boards.html')

@app.route('/manage-users')
def manage_users():
    return render_template('users.html')

if __name__ == '__main__':
    with app.app_context():
        print("여기 실행?")
        db.create_all()

    app.run(debug=True)