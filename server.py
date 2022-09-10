from flask import Flask,render_template
import requests
import json
from data import categorys 
app = Flask(__name__)


baseurl = "https://newsapi.org/v2/"

@app.template_filter()
def format_datetime(value, format='medium'):
     # Create a python date object to work on
    date_obj = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
    if format == 'full':
        return date_obj.strftime("%m/%d/%Y, %H:%M:%S")
    elif format == 'medium':
        return date_obj.strftime("%d-%b-%Y")

@app.template_filter()
def capfirst(value):
    return value[:1].upper()+value[1:]

@app.route("/")
def home():
    url = f'{baseurl}everything?q=country=in&apiKey={apiKey}'
    response_API = requests.get(url)
    data = response_API.text
    parse_json = json.loads(data)
    return render_template("index.html",newes=parse_json["articles"],categorys=categorys)