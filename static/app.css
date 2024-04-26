// Form and self-introduction text area
const form = document.querySelector("#form");
const selfIntroduction = document.querySelector("#self-introduction");

// Function to generate interview questions
// Fetch and handle interview questions, resume, and cover letter

// Function to generate interview questions
function generateInterviewQuestions() {
    const introduction = document.querySelector("#self-introduction").value;  // Get self-introduction

    const formData = new URLSearchParams();
    formData.append("introduction", introduction);  // Prepare POST data

    fetch("/generate_interview_questions", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",  // Content type for form data
        },
        body: formData,
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error("Failed to generate interview questions.");
        }
        return response.json();  // Parse JSON
    })
    .then((data) => {
        const output = document.querySelector("#interview-questions-output");
        output.innerHTML = data.interview_questions;  // Display interview questions with formatting
    })
    .catch((error) => {
        console.error("Error generating interview questions:", error);  // Handle errors
    });
}

// Function to generate resume
function generateResume() {
    const introduction = document.querySelector("#self-introduction").value;  // Get self-introduction

    const formData = new URLSearchParams();
    formData.append("introduction", introduction);  // Prepare POST data

    fetch("/generate_resume", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",  // Content type for form data
        },
        body: formData,
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error("Failed to generate resume.");
        }
        return response.json();  // Parse JSON
    })
    .then((data) => {
        const output = document.querySelector("#resume-output");
        output.innerHTML = data.resume.replace("<br>", "\n");  // Display resume with formatting
    })
    .catch((error) => {
        console.error("Error generating resume:", error);  // Handle errors
    });
}

// Function to generate cover letter
function generateCoverLetter() {
    const introduction = document.querySelector("#self-introduction").value;  // Get self-introduction

    const formData = new URLSearchParams();
    formData.append("introduction", introduction);  // Prepare POST data

    fetch("/generate_cover_letter", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",  // Content type for form data
        },
        body: formData,
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error("Failed to generate cover letter.");
        }
        return response.json();  // Parse JSON
    })
    .then((data) => {
        const output = document.querySelector("#cover-letter-output");
        output.innerHTML = data.cover_letter.replace("<br>", "\n");  // Display cover letter with formatting
    })
    .catch((error) => {
        console.error("Error generating cover letter:", error);  // Handle errors
    });
}

// Form submission event listener to prevent default behavior
form.addEventListener("submit", function (e) {
    e.preventDefault();  // Prevent default form submission
});
