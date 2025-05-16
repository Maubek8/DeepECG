from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analisar", methods=["POST"])
def analisar():
    if "file" not in request.files:
        return jsonify({"erro": "Arquivo não enviado."}), 400

    file = request.files["file"]
    headers = {
        "Authorization": "Bearer sk-6319e0794c7a498a8f1663660f5c287a"
    }
    files = {"file": (file.filename, file.stream, file.mimetype)}
    response = requests.post("https://api.deepseek.com/v1/axisecg/analisar", headers=headers, files=files)

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
