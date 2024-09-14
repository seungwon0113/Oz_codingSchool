from flask import Flask, request, render_template

app = Flask(__name__)

users = [
    {
        "username": "leo",
        "posts": [{"title": "Town House", "likes": 120}]
    },
    {
        "username": "alex",
        "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]
    },
    {
        "username": "kim",
        "posts": [{"title": "Delicious Ramen", "likes": 230}]
    }
]

@app.get('/')
def index():
    return render_template("index.html")

@app.get('/users')
def get_users():
    # 모든 사용자 정보를 JSON 형태로 반환
    return {"users": users}

@app.post('/users')
def create_user():
    # 클라이언트로부터 받은 JSON 데이터
    request_date = request.get_json()

    # 새 사용자 객체 생성
    new_user = {"username":request_date["username"], "posts": [{"title": "My First Post", "likes": 0}]}

    # 사용자 리스트에 새 사용자 추가
    users.append(new_user)

    # 생성한 사용자 정보와 HTTP 상태코드 201 반환
    return new_user, 201

@app.post('/users/post/<string:username>')
def add_post(username):
    pass