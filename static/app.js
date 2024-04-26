// 获取表单和按钮
const introductionField = document.querySelector("#introduction");
const generateInterviewQuestionsBtn = document.querySelector("#generate-interview-questions");
const generateResumeBtn = document.querySelector("#generate-resume");

// 为生成面试问题的按钮添加事件监听器
generateInterviewQuestionsBtn.addEventListener("click", function () {
  generateInterviewQuestions(); // 调用生成面试问题的函数
});

// 为生成简历的按钮添加事件监听器
generateResumeBtn.addEventListener("click", function () {
  generateResume(); // 调用生成简历的函数
});

// 生成面试问题的函数
// 生成面试问题的函数
function generateInterviewQuestions() {
    const introduction = document.querySelector("#introduction").value; // 获取自我介绍内容

    fetch("/generate_interview_questions", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({ introduction }), // 发送自我介绍
    })
        .then((response) => response.json()) // 解析响应为 JSON
        .then((data) => {
            const interviewQuestionsOutput = document.querySelector("#interview-questions-output"); // 面试问题输出区域
            interviewQuestionsOutput.innerHTML = ""; // 清空之前的内容

            const questions = data.interview_questions.split('\n'); // 将面试问题拆分为数组
            questions.forEach((question) => {
                const listItem = document.createElement("li"); // 创建列表项
                listItem.textContent = question; // 设置列表项内容
                interviewQuestionsOutput.appendChild(listItem); // 添加到输出区域
            });
        })
        .catch((error) => {
            console.error("Error generating interview questions:", error); // 错误处理
        });
}

// 生成简历的函数
function generateResume() {
    const introduction = document.querySelector("#introduction").value; // 获取自我介绍内容

    fetch("/generate_resume", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({ introduction }), // 发送自我介绍
    })
        .then((response) => response.json()) // 解析响应为 JSON
        .then((data) => {
            const resumeOutput = document.querySelector("#resume-output"); // 简历输出区域
            resumeOutput.innerHTML = ""; // 清空之前的内容

            const resumeElement = document.createElement("pre"); // 使用 <pre> 保持格式
            resumeElement.textContent = data.resume; // 设置简历内容
            resumeOutput.appendChild(resumeElement); // 添加到输出区域
        })
        .catch((error) => {
            console.error("Error generating resume:", error); // 错误处理
        });
}
