function redirectToInterview() {
    // console.log(JSON.stringify(window.location));
    const targetPath = '/interview';  // 리다이렉션할 경로

    // const targetUrl = `http://${targetHost}:${targetPort}${targetPath}`;
    const targetUrl = "https://" + window.location.hostname + targetPath;
    console.log(targetUrl);
    window.location.href = targetUrl;
    
}