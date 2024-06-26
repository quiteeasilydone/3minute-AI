var submit = document.getElementById('submit-button');
submit.onclick = submitPortfolio;

var analysis = document.getElementById('analysis-button');
analysis.onclick = portfolioAnalysis;

url = "http://165.246.44.125:80/api/upload";

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
    newImage.style.display = "block";

    container.appendChild(newImage);
    console.log(newImage.src);
    uploadFile(file);
    // uploadFile('hi');
}

async function uploadFile(file) {
    var formData = new FormData()
    formData.append('file', file);
    try{
        const response = await fetch(url, {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const jsonResponse = await response.json();
            alert(`File uploaded successfully: ${jsonResponse.filename}`);
        } else {
            alert('File upload failed!');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while uploading the file.');
    }
    
}