from flask import Flask,render_template
import requests
import json
app = Flask(__name__)

url = "https://newsapi.org/v2/"

@app.route("/")
def home():
    url = f'https://newsapi.org/v2/everything?q=country=in&apiKey={apiKey}'
    response_API = requests.get(url)
    data = response_API.text
    parse_json = json.loads(data)
    return render_template("index.html",newes=parse_json["articles"])