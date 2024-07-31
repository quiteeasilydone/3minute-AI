function redirectToInformation() {
    // console.log(JSON.stringify(window.location));
    const targetPath = '/information';  // 리다이렉션할 경로

    // const targetUrl = `http://${targetHost}:${targetPort}${targetPath}`;
    const targetUrl = "https://" + window.location.hostname + targetPath;
    console.log(targetUrl);
    window.location.href = targetUrl;
    
}

function redirectToAPI() {
    // console.log(JSON.stringify(window.location));
    const targetPath = '/api-key';  // 리다이렉션할 경로

    // const targetUrl = `http://${targetHost}:${targetPort}${targetPath}`;
    const targetUrl = "https://" + window.location.hostname + targetPath;
    console.log(targetUrl);
    window.location.href = targetUrl;
    
}

document.addEventListener('DOMContentLoaded', () => {
    sessionStorage.clear()
})