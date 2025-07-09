const form = document.getElementById('proxy-form');
const urlInput = document.getElementById('urlInput');
const proxyFrame = document.getElementById('proxy-frame');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const url = urlInput.value;
    if (url) {
        proxyFrame.src = `https://api.allorigins.win/raw?url=${encodeURIComponent(url)}`;
    }
});