document.addEventListener('DOMContentLoaded', () => {
    const feedbackArray = JSON.parse(sessionStorage.getItem('feedback')) || [];
    let currentIndex = 0;

    const questionText = document.getElementById('question-text');
    const answerText = document.getElementById('answer-text');
    const feedbackText = document.getElementById('feedback-text');
    const exampleText = document.getElementById('example-text');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');

    function displayFeedback(index) {
        if (index < 0 || index >= feedbackArray.length) return;
        const feedback = feedbackArray[index];
        questionText.textContent = feedback.question;
        answerText.textContent = feedback.answer;
        feedbackText.textContent = feedback.feedback;
        exampleText.textContent = feedback.example;

        prevBtn.disabled = (index === 0);
        nextBtn.disabled = (index === feedbackArray.length - 1);
    }

    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            displayFeedback(currentIndex);
        }
    });

    nextBtn.addEventListener('click', () => {
        if (currentIndex < feedbackArray.length - 1) {
            currentIndex++;
            displayFeedback(currentIndex);
        }
    });

    // 초기 피드백 표시
    displayFeedback(currentIndex);
});