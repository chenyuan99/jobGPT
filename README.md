# jobGPT
A Job Seeking Tool Powered by GPT presented by [OfferPlus](https://offersplus.xyz)

## Componenents

- interviewGPT （private)

- resumeGPT (public)

## Key Features
- **Generate Interview Questions**: Input your self-introduction, and the app generates 10 interview questions tailored to your background.
- **Create a Resume**: Provide answers to the interview questions, and the app creates a personalized resume for you.
- **Flexible and Dynamic**: The app adjusts its questions and resume structure based on your responses, allowing for a more personalized experience.
- **Interactive User Interface**: With a simple and intuitive design, users can quickly generate interview questions and resumes with just a few clicks.
- **OpenAI-Powered**: Leverages GPT-3.5-turbo to ensure high-quality question generation and resume content.

## How It Works
The application uses Flask, a lightweight web framework for Python, to handle server-side logic. It communicates with OpenAI's GPT model to generate questions and build resumes. Here's how it works:
1. **Generate Interview Questions**: The app takes your self-introduction and generates a set of 10 interview questions that cover various topics like education, work experience, skills, and career goals.
2. **Answer Interview Questions**: You fill in the answers to the generated questions, providing as much detail as possible.
3. **Generate Resume**: The app extracts key information from your answers and creates a resume in markdown format. The resume includes sections like Personal Information, Education, Work Experience, Skills, Projects, Teamwork, Leadership, Problem Solving, Personal Achievements, and Career Goals.

## Benefits
- **Time-Saving**: Quickly create interview questions and resumes without manual effort.
- **Customizable**: Adjust the interview questions and resume content based on your personal experiences and career goals.
- **Professional Output**: Generates a well-structured resume suitable for job applications.

## Use Cases
- **Job Seekers**: Prepare for interviews and create resumes for job applications.
- **Career Coaches**: Use the app to guide clients in preparing for interviews and building resumes.
- **HR Professionals**: Generate interview questions based on candidate introductions for a more personalized interview process.

