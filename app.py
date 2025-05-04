from flask import Flask, request, send_file, send_from_directory
import os, subprocess, uuid

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return {"error": "URL is required"}, 400

    filename = f"{uuid.uuid4().hex}.pdf"
    filepath = os.path.join("/tmp", filename)

    try:
        subprocess.run(["wkhtmltopdf", url, filepath], check=True)
        return send_file(filepath, as_attachment=True, download_name="converted.pdf")
    except subprocess.CalledProcessError as e:
        return {"error": "Conversion failed"}, 500
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
