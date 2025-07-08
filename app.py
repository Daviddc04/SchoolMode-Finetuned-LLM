# app.py
from flask import Flask, request, jsonify, render_template
from chat import chat_with_model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")
    edu_mode = data.get("education_mode", False)
    response = chat_with_model(prompt, education_mode=edu_mode)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
