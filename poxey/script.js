const urlInput = document.getElementById('urlInput');
const proxyButton = document.getElementById('proxyButton');

proxyButton.addEventListener('click', () => {
    const url = urlInput.value;
    if (url) {
        window.location.href = `/proxy?url=${encodeURIComponent(url)}`;
    }
});