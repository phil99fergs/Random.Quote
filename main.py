from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_BASE_URL = "https://api.quotable.io"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quote")
def quote():
    author = request.args.get("author")
    url = f"{API_BASE_URL}/random"
    if author:
        url += f"?author={author}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = {"text": data["content"], "author": data["author"]}
        return jsonify(quote)
    else:
        error_message = "There is no such author in database or you have written the author's name incorrectly."
        return jsonify({"error": error_message})



if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8000)
