document.getElementById('submit-button').onclick = submitPortfolio;
document.getElementById('analysis-button').onclick = portfolioAnalysis;

let filename = '';

function fillInBlankDiv(divId, targetList) {
    const targetDiv = document.getElementById(divId);
    targetDiv.innerHTML = '';
    targetList.forEach(element => {
        const listItem = document.createElement('p');
        listItem.innerText = element;
        targetDiv.appendChild(listItem);
    });
}

async function portfolioAnalysis() {
    const loadingDiv = document.getElementById('loading');
    const url = new URL("https://" + window.location.hostname + "/api/portfolio-analysis");
    const encodedFilename = encodeURIComponent(filename);
    const apiKey = sessionStorage.getItem('apiKey')

    url.searchParams.append("filename", encodedFilename);
    url.searchParams.append('apiKey', apiKey)

    const nameDiv = document.getElementById('name-container');
    const divList = {
        "major-container": "전공",
        "project-container": "직무경험",
        "special-container": "기타"
    };

    try {
        loadingDiv.style.display = 'block';
        const response = await fetch(url, { method: 'GET' });

        if (response.ok) {
            const jsonResponse = await response.json();
            alert('이력서 분석이 완료되었습니다!');
            nameDiv.innerText = jsonResponse['이름'];

            Object.entries(divList).forEach(([key, value]) => {
                fillInBlankDiv(key, jsonResponse[value]);
            });
        } else {
            alert('이력서 분석에 실패했습니다.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while uploading the file.');
    } finally {
        loadingDiv.style.display = 'none';
    }
}

async function submitPortfolio() {
    const loadingDiv = document.getElementById('loading');
    const requsetBody = {
        "name": document.getElementById('name-container').innerText,
        "major": document.getElementById('major-container').innerText,
        "job": document.getElementById('job-container').innerText,
        "project": document.getElementById('project-container').innerText,
        "special": document.getElementById('special-container').innerText
    };

    const apiKey = sessionStorage.getItem('apiKey')
    requsetBody.apiKey = apiKey

    const url = new URL("https://" + window.location.hostname + "/api/generate-interview-question");

    try {
        loadingDiv.style.display = 'block';
        const response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify(requsetBody),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            const jsonResponse = await response.json();
            alert('이력서 기반 면접 질문이 생성되었습니다.');

            sessionStorage.setItem('info', JSON.stringify(requsetBody));

            const intro = ["간단한 자기소개 부탁드립니다."];
            const jobArray = jsonResponse["직무질문"];
            const techArray = jsonResponse['기술질문'];
            const attitudeArray = jsonResponse['인성질문'];

            const questionArray = [...intro, ...jobArray, ...techArray, ...attitudeArray];
            sessionStorage.setItem("questions", JSON.stringify(questionArray));

            window.location.replace(`https://${window.location.hostname}/pre-interview`)
        } else {
            alert('Analysis failed!');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while uploading the file.');
    } finally {
        loadingDiv.style.display = 'none';
    }
}

function loadFile(input) {
    const container = document.getElementById('image-show');
    container.innerHTML = '';
    const file = input.files[0];

    const newImage = document.createElement("img");
    newImage.classList.add('img');
    newImage.src = URL.createObjectURL(file);
    Object.assign(newImage.style, {
        width: "70%",
        height: "70%",
        visibility: "visible",
        objectFit: "contain",
        margin: "auto",
        display: "block"
    });

    container.appendChild(newImage);
    filename = file.name;
    uploadFile(file);
}

async function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch("/api/upload", {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            console.log('upload complete');
        } else {
            alert('File upload failed!');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while uploading the file.');
    }
}