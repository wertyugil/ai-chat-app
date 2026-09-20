from flask import Flask, request, jsonify
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def home():
    return open("/data/data/com.termux/files/home/MagicSkills/index.html").read()

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message", "")
    data = json.dumps({
        "model": "tinyllama",
        "messages": [{"role": "user", "content": msg}],
        "stream": False
    }).encode()
    req = urllib.request.Request(
        "http://127.0.0.1:11434/api/chat",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    res = json.loads(urllib.request.urlopen(req).read())
    return jsonify({"reply": res["message"]["content"]})

app.run(host="127.0.0.1", port=8080)
