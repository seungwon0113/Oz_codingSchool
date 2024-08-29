# command + shift + p => python3 select interpreter

from flask import Flask, request, Response

app = Flask(__name__)

# hosr , post 지정
# 127.0.0.1:5000 = 127.0.0.1:localhost 라고도 불리며 내컴퓨터를 가르킨다.
# host = '127.0.0.1'
# port = '8000'

# 라우팅 (Route) : URL과 특정함수 간의 매핑을 정의
@app.route('/')
def home():
    return "Hello, This is Main Page!"

@app.route('/about')
def about():
    return "This is about page!"

# 동적으로 URL parameter value를 밭아서 처리해준다.
# http://127.0.0.1:5000/user/seungwon
@app.route('/user/<username>')
def user_profile(username):
    return f"UserName : {username}"


# post 요청 날리는 법
# 1) postman
# 2) requests
import requests # pip install requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data) # requests 요청을 날리면 response가 와야한다

    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)
    
    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("***POST method***", request.data)

    return Response("Sucessfully submitted", status=200)

    if request.method == 'PUT':
        print("PUT method")

    if request.method == 'DELETE':
        print("DELETE method")

if __name__ == '__main__':
    print('__name__', __name__)
    app.run() # host, port 지정 : run(host+host, port=port)

# FLASK 실행
# 1) python -m flask
# 2) flask run
# 3) flask --app app.py --debug run
# 4) 직접 실행법 : python your_app.py

