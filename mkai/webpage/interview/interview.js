document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chat-container');
    const loadingDiv = document.getElementById('loading');
    const resultContainer = document.getElementById('result-container');
    const submitBtn = document.getElementById('submit-btn');
    const answerInput = document.getElementById('answer');
    const questionElement = document.getElementById('question');

    sessionStorage.setItem('currentIndex', 0);
    const feedbackArray = [];

    answerInput.addEventListener("keyup", (event) => {
        if (event.keyCode === 13) {
            event.preventDefault();
            submitBtn.click();
        }
    })

    function showNextQuestion() {
        const currentIndex = parseInt(sessionStorage.getItem('currentIndex'), 10);
        const questions = JSON.parse(sessionStorage.getItem('questions'));
        questionElement.textContent = questions[currentIndex];
    }

    async function fetchAndProcess(url, requestBody) {
        const apiKey = sessionStorage.getItem('apiKey')
        requestBody.apiKey = apiKey
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestBody)
            });

            if (response.ok) {
                return await response.json();
            } else {
                console.log('Request failed');
            }
        } catch (error) {
            console.log('Error:', error);
        }
    }

    async function showTailQuestion() {
        const url = `https://${window.location.hostname}/api/question/follow-question`;
        const requestBody = { ...JSON.parse(sessionStorage.getItem('info')) };
        requestBody.question = questionElement.textContent;
        requestBody.answer = answerInput.value;

        const jsonResponse = await fetchAndProcess(url, requestBody);
        if (jsonResponse) {
            questionElement.textContent = jsonResponse.follow_question;
        }
    }

    async function getFeedback() {
        const feedbackUrl = `https://${window.location.hostname}/api/question/feedback`;
        const feedbackRequestBody = { ...JSON.parse(sessionStorage.getItem('info')) };
        feedbackRequestBody.question = questionElement.textContent;
        feedbackRequestBody.answer = answerInput.value;

        const feedbackJsonResponse = await fetchAndProcess(feedbackUrl, feedbackRequestBody);
        if (feedbackJsonResponse) {
            const { feedback, example_answer: example } = feedbackJsonResponse;
            feedbackArray.push({
                question: feedbackRequestBody.question,
                answer: feedbackRequestBody.answer,
                feedback,
                example
            });
        }
    }

    submitBtn.addEventListener('click', async () => {
        const getTailQuestion = Math.floor(Math.random() * 2);
        const currentIndex = parseInt(sessionStorage.getItem('currentIndex'), 10);
        const questions = JSON.parse(sessionStorage.getItem('questions'));

        loadingDiv.style.display = 'block';
        answerInput.disabled = true;
        submitBtn.disabled = true;

        if (currentIndex >= questions.length - 1) {
            await getFeedback();
            sessionStorage.setItem('feedback', JSON.stringify(feedbackArray))
            window.location.href = `https://${window.location.hostname}/feedback`
        } else {
            if (getTailQuestion === 0) {
                sessionStorage.setItem('currentIndex', currentIndex + 1);
                getFeedback();
                showNextQuestion();
            } else {
                getFeedback();
                await showTailQuestion();
            }
            answerInput.value = '';
        }

        loadingDiv.style.display = 'none';
        answerInput.disabled = false;
        submitBtn.disabled = false;
    });

    showNextQuestion();
});