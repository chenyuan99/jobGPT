from app import db  # 引入 SQLAlchemy
from datetime import datetime


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 初始化SQLAlchemy
db = SQLAlchemy()

# 用户模型
class User(db.Model):
    __tablename__ = 'users'  # 表名称

    id = db.Column(db.Integer, primary_key=True)  # 用户ID
    username = db.Column(db.String(100), unique=True, nullable=False)  # 用户名
    password = db.Column(db.String(255), nullable=False)  # 密码
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # 创建时间



