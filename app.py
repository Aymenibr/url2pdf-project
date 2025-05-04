from flask import Flask, request, send_file
import os
import subprocess
import uuid

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return {"error": "No URL provided"}, 400

    # Generate unique filename
    filename = f"{uuid.uuid4().hex}.pdf"
    filepath = os.path.join("/tmp", filename)

    try:
        # Convert URL to PDF using wkhtmltopdf
        subprocess.run(["wkhtmltopdf", url, filepath], check=True)

        return send_file(filepath, as_attachment=True, download_name=filename)

    except subprocess.CalledProcessError:
        return {"error": "Conversion failed"}, 500

    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
