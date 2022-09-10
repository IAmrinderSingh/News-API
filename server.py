from flask import Flask,render_template
import requests
import json
from data import categorys 
app = Flask(__name__)

baseurl = "https://newsapi.org/v2/"

@app.route("/")
def home():
    url = f'{baseurl}everything?q=country=in&apiKey={apiKey}'
    response_API = requests.get(url)
    data = response_API.text
    parse_json = json.loads(data)
    return render_template("index.html",newes=parse_json["articles"],categorys=categorys)