from dotenv import dotenv_values
from flask import Flask, render_template, request, jsonify
import openai
import json

# Load OpenAI API key
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

# Create Flask app
app = Flask(__name__, template_folder="templates", static_url_path="", static_folder="static")

# Generate interview questions from self-introduction
def generate_interview_questions_from_intro(introduction):
    prompt = f"""
    Based on the following self-introduction, generate 10 interview questions:

    {introduction}

    Make sure the questions cover key topics like education, work experience, skills, projects, achievements, teamwork, leadership, and career goals.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    interview_questions = response["choices"][0]["message"]["content"].strip().replace("\n", "<br>")
    return interview_questions

# Generate resume based on self-introduction
def generate_resume_from_intro(introduction):
    prompt = f"""
    Create a resume based on the following self-introduction:

    {introduction}

    Include sections for Personal Information, Education, Work Experience, Skills, Projects, Teamwork, Leadership, Problem Solving, Personal Achievements, and Career Goals.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    resume = response["choices"][0]["message"]["content"].strip().replace("\n", "<br>")
    return resume

# Generate cover letter based on self-introduction
def generate_cover_letter_from_intro(introduction):
    prompt = f"""
    Create a cover letter based on the following self-introduction:

    {introduction}

    Include a greeting, background summary, reasons for interest in the position, and a closing statement.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    cover_letter = response["choices"][0]["message"]["content"].strip().replace("\n", "<br>")
    return cover_letter

# Flask endpoint for generating interview questions
@app.route("/generate_interview_questions", methods=["POST"])
def generate_interview_questions():
    introduction = request.form.get("introduction", "")  # Get self-introduction
    interview_questions = generate_interview_questions_from_intro(introduction)  # Generate interview questions
    return jsonify({"interview_questions": interview_questions})

# Flask endpoint for generating resume
@app.route("/generate_resume", methods=["POST"])
def generate_resume():
    introduction = request.form.get("introduction", "")  # Get self-introduction
    resume = generate_resume_from_intro(introduction)  # Generate resume
    return jsonify({"resume": resume})

# Flask endpoint for generating cover letter
@app.route("/generate_cover_letter", methods=["POST"])
def generate_cover_letter():
    introduction = request.form.get("introduction", "")  # Get self-introduction
    cover_letter = generate_cover_letter_from_intro(introduction)  # Generate cover letter
    return jsonify({"cover_letter": cover_letter})

# Render the main page
@app.route("/")
def index():
    return render_template("index.html")

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)  # Start Flask app
