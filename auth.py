from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import User  # 用户模型
from app import db, bcrypt  # 数据库和密码加密
from sqlalchemy.exc import IntegrityError

# 创建身份验证蓝图
auth_bp = Blueprint('auth', __name__)

# 路由：用户注册
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # 使用 Bcrypt 加密密码
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # 创建新用户
        new_user = User(username=username, password=hashed_password)

        try:
            db.session.add(new_user)  # 添加用户
            db.session.commit()  # 提交更改
            flash('Registration successful!', 'success')  # 注册成功
            return redirect(url_for('auth.login'))  # 重定向到登录页面
        except IntegrityError:  # 用户名重复
            db.session.rollback()  # 回滚更改
            flash('Username already exists.', 'danger')  # 错误信息

    return render_template('register.html')  # 显示注册页面

# 路由：用户登录
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # 查找用户
        user = User.query.filter_by(username=username).first()

        # 验证密码
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id  # 存储用户ID在会话中
            flash('Login successful!', 'success')  # 登录成功
            return redirect(url_for('index'))  # 重定向到主页
        else:
            flash('Invalid username or password.', 'danger')  # 错误信息

    return render_template('login.html')  # 显示登录页面

# 路由：用户注销
@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)  # 移除用户ID
    flash('Logged out successfully.', 'success')  # 注销成功
    return redirect(url_for('index'))  # 重定向到主页
