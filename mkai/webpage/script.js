function redirectToInformation() {
    // console.log(JSON.stringify(window.location));
    const targetHost = '165.246.44.125';
    const targetPort = 81;
    const targetPath = '/information';  // 리다이렉션할 경로

    // const targetUrl = `http://${targetHost}:${targetPort}${targetPath}`;
    const targetUrl = "http://" + targetHost + ":" + targetPort + targetPath + "/";
    console.log(targetUrl);
    window.location.href = targetUrl;
    
}