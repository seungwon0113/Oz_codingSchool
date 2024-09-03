from flask import Flask, render_template
from flask_mysqldb import MySQL
import yaml
from flask_smorest import Api
from posts_routes import create_posts_blueprint

app = Flask(__name__)

# db 등록
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config["MYSQL_HOST"] = db['mysql_host']
app.config["MYSQL_USER"] = db['mysql_user']
app.config["MYSQL_PASSWORD"] = db['mysql_password']
app.config["MYSQL_DB"] = db['mysql_db']

# 불러오기
mysql = MySQL(app)

# Blueprint 설정
app.config['API_TITLE'] = 'Blog API List'
app.config['API_VERSION'] = '1.0'
app.config['OPENAPI_VERSION'] = '3.1.3'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] ='/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdeliver.net/npm/swagger-ui-dist/"

api = Api(app)
posts_blp = create_posts_blueprint(mysql)
api.register_blueprint(posts_blp) # api 등록

@app.route('/blogs')
def manager_blogs():
    return render_template("posts.html")

if __name__ == '__main__':
    app.run(debug=True)