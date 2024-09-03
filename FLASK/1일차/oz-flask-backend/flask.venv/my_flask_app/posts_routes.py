from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_posts_blueprint(mysql):
    # Blueprint 작성
    posts_blp = Blueprint("posts", __name__, description='Posts API', url_prefix='/posts')

    @posts_blp.route('/', methods=['GET', 'POST'])
    def posts():
        cursor = mysql.connection.cursor()

        # 게시글 조회
        if request.method == 'GET':
            sql = "SELECT * FROM posts"
            cursor.execute(sql)

            posts = cursor.fetchall()
            cursor.close()

            posts_list = [
                {'id': post[0], 'title': post[1], 'content': post[2]}
                for post in posts
            ]

            return jsonify(posts_list)

        # 게시글 생성
        elif request.method == 'POST':
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, message="Title or Content cannot be empty")

            sql = 'INSERT INTO posts(title, content) VALUES(%s, %s)'
            cursor.execute(sql, (title, content))
            mysql.connection.commit()
            cursor.close()

            return jsonify({'msg': "Successfully created post", "title": title, "content": content}), 201

    @posts_blp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def post(id):
        cursor = mysql.connection.cursor()

        # SQL Injection 방지
        sql = "SELECT * FROM posts WHERE id = %s"
        cursor.execute(sql, (id,))
        post = cursor.fetchone()

        if not post:
            cursor.close()
            abort(404, message="Post not found")

        if request.method == 'GET':
            cursor.close()
            return jsonify({'id': post[0], 'title': post[1], 'content': post[2]})

        elif request.method == 'PUT':
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                cursor.close()
                abort(400, message="Title and Content cannot be empty")

            sql = "UPDATE posts SET title=%s, content=%s WHERE id=%s"
            cursor.execute(sql, (title, content, id))
            mysql.connection.commit()
            cursor.close()

            return jsonify({"msg": "Successfully updated post"})

        elif request.method == 'DELETE':
            sql = "DELETE FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            mysql.connection.commit()
            cursor.close()

            return jsonify({"msg": "Successfully deleted post"})

    return posts_blp
