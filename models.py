from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()  # SQLAlchemy를 사용해 데이터베이스 저장

class User(db.Model):  # 데이터 모델을 나타내는 객체 선언
    __tablename__ = 'user_table'  # 테이블 이름

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    following_list = db.Column(db.String(400))

    def __init__(self, userid, password, **kwargs):
        self.userid = userid
        self.set_password(password)
        self.following_list = ""

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def set_userid(self, userid):
        self.userid = userid
        
    def add_following(self, userid):
        self.following_list = list_to_string(self.following_list.split().append(userid))
    
    def get_following(self):
        return self.following_list.split()
