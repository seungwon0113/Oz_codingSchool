from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 임시 사용자 데이터
users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

# 사용자 추가, 수정, 삭제 라우트 및 함수 작성...

# 사용자 츄가 뷰
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        users.append({'username':username, 'name':name})
        return redirect(url_for('index'))
    return render_template('add_user.html')

# 사용자 수정 뷰
@app.route('/edit/<username>', methods=['GET','POST'])
def edit_user(username):
    user = next((user for user in users if user['username'] == username), None)
    if not user:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        user['name'] = request.form['name']
        return redirect(url_for('index'))
    
    return render_template('edit_user.html', user=user)

# 사용자 삭제 뷰
@app.route('/delete/<username>')
def delete_user(username):
    global users
    users = [user for user in users if user['username'] != username]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)