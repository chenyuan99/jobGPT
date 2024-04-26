from dotenv import dotenv_values
from flask import Flask, render_template, request, jsonify
import openai
import json

# 加载 OpenAI API 密钥
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

# 创建 Flask 应用
app = Flask(__name__, template_folder="templates", static_url_path="", static_folder="static")

# 使用自我介绍生成面试问题
def generate_interview_questions_from_intro(introduction):
    # 定义 GPT 提示
    prompt = f"""
    Based on the following self-introduction, generate 10 interview questions:

    {introduction}

    Ensure the questions cover key resume topics like education, work experience, skills, projects, achievements, teamwork, leadership, and career goals.
    """

    # 通过 OpenAI 的 ChatCompletion 生成面试问题
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    interview_questions = response["choices"][0]["message"]["content"].strip()
    return interview_questions

# 使用自我介绍生成简历
def generate_resume_from_intro(introduction):
    # 定义 GPT 提示
    prompt = f"""
    Create a resume based on the following self-introduction:

    {introduction}

    Ensure the resume covers key sections like Personal Information, Education, Work Experience, Skills, Projects, Teamwork, Leadership, Problem Solving, Personal Achievements, and Career Goals.
    """

    # 通过 OpenAI 的 ChatCompletion 生成简历
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    resume = response["choices"][0]["message"]["content"].strip()
    return resume

# Flask 路由，用于生成面试问题
@app.route("/generate_interview_questions", methods=["POST"])
def prompt_to_generate_interview_questions():
    introduction = request.form.get("introduction", "")  # 获取用户的自我介绍
    interview_questions = generate_interview_questions_from_intro(introduction)  # 生成面试问题
    return jsonify({"interview_questions": interview_questions})

# Flask 路由，用于生成简历
@app.route("/generate_resume", methods=["POST"])
def prompt_to_generate_resume():
    introduction = request.form.get("introduction", "")  # 获取自我介绍
    resume = generate_resume_from_intro(introduction)  # 生成简历
    return jsonify({"resume": resume})

# 渲染主页
@app.route("/")
def index():
    return render_template("index.html")

# 运行 Flask 应用
if __name__== "__main__":
    app.run(debug=True)  # 启动 Flask 应用
