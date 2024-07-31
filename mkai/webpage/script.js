function redirectToMain() {
    window.location.href = `https://${window.location.hostname}`; // 메인 페이지로 리디렉션
}

function checkApiKey() {
    const apiKey = sessionStorage.getItem('apiKey');
    if (!apiKey) {
        alert('API 키가 없습니다. 메인 페이지로 이동합니다.');
        redirectToMain();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    checkApiKey(); // 페이지 로드 시 API 키 확인
});

// window.addEventListener('beforeunload', (event) => {
//     const message = '이 페이지를 떠나시겠습니까? 변경 사항이 저장되지 않을 수 있습니다.';
//     event.returnValue = message;
//     return message;
// });

window.addEventListener('popstate', (event) => {
    const message = '페이지를 떠나시겠습니까? 변경 사항이 저장되지 않을 수 있습니다.';
    if (confirm(message)) {
        window.location.href = `https://${window.location.hostname}`; // 메인 페이지 URL로 변경
    } else {
        history.pushState(null, null, window.location.href);
    }
});

// 현재 상태를 히스토리에 추가하여 popstate 이벤트를 트리거할 수 있도록 합니다.
history.pushState(null, null, window.location.href);