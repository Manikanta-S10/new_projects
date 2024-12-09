from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/post")
def home():
    response = requests.get(url=" https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("index.html",posts=data)

@app.route("/body/<num>")
def paragraphs(num):
    response = requests.get(url=" https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("para.html",posts=data,number=int(num))
    

if __name__ == "__main__":
    app.run(debug=True)

