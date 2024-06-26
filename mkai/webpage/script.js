function redirectToInformation() {
    // console.log(JSON.stringify(window.location));
    const targetHost = '165.246.44.125';
    const targetPort = 80;
    const targetPath = '/information';  // 리다이렉션할 경로

    // const targetUrl = `http://${targetHost}:${targetPort}${targetPath}`;
    const targetUrl = "http://" + targetHost + ":" + targetPort + targetPath + "/";
    console.log(targetUrl);
    window.location.href = targetUrl;
    
}

function redirectToPortfolio() {
    // console.log(JSON.stringify(window.location));
    const targetHost = '165.246.44.125';
    const targetPort = 80;
    const targetPath = '/upload-portfolio';  // 리다이렉션할 경로

    // const targetUrl = `http://${targetHost}:${targetPort}${targetPath}`;
    const targetUrl = "http://" + targetHost + ":" + targetPort + targetPath + "/";
    console.log(targetUrl);
    window.location.href = targetUrl;
    
}