var submit = document.getElementById('submit-button');
submit.onclick = submitPortfolio;

var analysis = document.getElementById('analysis-button');
analysis.onclick = portfolioAnalysis;


function portfolioAnalysis() {

}

function submitPortfolio() {
    var name = document.getElementById('name-container').innerText
    var major = document.getElementById('major-container').innerText
    var job = document.getElementById('job-container').innerText
    var project = document.getElementById('project-container').innerText
    var special = document.getElementById('special-container').innerText

    let portfolio = {"name" : name, "major" : major, "job" : job, "project" : project, "special" : special}

    console.log(portfolio)
}

function loadFile(input) {
    var container = document.getElementById('image-show');
    container.innerHTML = ''
    var file = input.files[0];

    var newImage = document.createElement("img");
    newImage.setAttribute("class", 'img');

    newImage.src = URL.createObjectURL(file);   

    newImage.style.width = "70%";
    newImage.style.height = "70%";
    newImage.style.visibility = "visible";
    newImage.style.objectFit = "contain";
    newImage.style.margin = "auto";
    newImage.style.display = "block"

    container.appendChild(newImage);
    uploadFile(file);
}

async function uploadFile(file) {
    const formData = new FormData()
    formData.append("portfolio", file)

    try {
        const response = await fetch('url', {
            method: 'POST',
            body: formData
        });
        if (response.ok) {
            const result = await response.json();
            console.log('업로드 성공!', result);
        } else {
            console.error('업로드 실패', response.statusText);
        }
    } catch (error) {
        console.error('에러 발생', error);
    }
}