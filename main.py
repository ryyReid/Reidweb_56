from flask import Flask, request, send_file, send_from_directory
import requests
import io

# Use the 'poxey' directory to serve the frontend files
app = Flask(__name__, static_folder='poxey', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('poxey', 'index.html')

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return "No URL provided.", 400

    # Add http:// if no scheme is present
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    try:
        response = requests.get(url, stream=True)
        # Pass through the content from the requested URL
        return send_file(
            io.BytesIO(response.content),
            mimetype=response.headers.get('Content-Type', 'application/octet-stream')
        )
    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    print("Starting proxy server on http://localhost:8080")
    app.run(port=8080)