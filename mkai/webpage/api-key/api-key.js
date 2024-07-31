function saveApiKey() {
    const apiKey = document.getElementById('api-key-input').value;
    if (apiKey) {
        sessionStorage.setItem('apiKey', apiKey);
        alert('API 키가 저장되었습니다.');
        redirectToPortfolio()
    } else {
        alert('API 키를 입력해주세요.');
    }
}

function redirectToPortfolio() {
    window.location.href = `https://${window.location.hostname}/upload-portfolio`; // 실제 시작하기 페이지로 리디렉션
}