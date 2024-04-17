import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from openai import OpenAI
import os
from trulens_eval import Provider, TruLlama, FeedbackMode, Feedback, Select,  Tru
from trulens_eval.feedback import Groundedness
from trulens_eval import OpenAI as fOpenAI
import pandas as pd
import numpy as np
from tqdm import tqdm
from pydantic import GetCoreSchemaHandler, TypeAdapter

from app import *

from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

# 使用正确的键名获取环境变量
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")




# 初始化Flask应用和SQLAlchemy
app = Flask(__name__)

# 设置Flask配置

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # 指定SQLite数据库文件
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁用警告
app.secret_key = os.getenv('FLASK_SECRET_KEY', x)
# 初始化SQLAlchemy和Bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# 使用Flask-Migrate
migrate = Migrate(app, db)  # 支持数据库迁移

# 延迟导入和注册蓝图
def create_app():
    with app.app_context():  # 确保在Flask应用上下文中
        from auth import auth_bp  # 延迟导入用户身份验证模块
        app.register_blueprint(auth_bp)  # 注册蓝图

    return app

# 主路由
@app.route('/')
def index():
    return "Welcome to the Flask App!"

# 生成文本路由
@app.route('/generate_text', methods=['POST'])
def generate_text():
    from flask import request, jsonify
    import openai

    prompt = request.json.get('prompt', '')  # 获取提示

    openai.api_key = os.getenv('OPENAI_API_KEY', 'y')  # OpenAI API密钥
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )

    generated_text = response['choices'][0]['text']
    return jsonify({'generated_text': generated_text})  # 返回生成的文本

# Flask应用程序的入口点
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # 启动Flask应用
