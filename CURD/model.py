""" 
ORM (Object Relational Mapping) 可以將資料庫當作物件來操作
"""

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

# 取得目前文件資料夾的路徑
pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# 若沒設定有可能會出現異常
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 設定sqlite檔案路徑
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(pjdir, 'data.sqlite')

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(64), unique=True, nullable=False)
    email = db.Column(db.VARCHAR(80), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' %self.username


## build sqlite : data.sqlite ##
################################
# 從Flask-SQLAlchemy 3.0開始須對 db.engine(or db.session)的訪問進行活動的Flask應用程式上下文管理
# db.create_all() 使用 db.engine

def init_db():
    with app.app_context():
        db.create_all()

# init_db()