from flask import Flask,render_template
import requests
import json
from data import categorys 
import datetime
app = Flask(__name__)


baseurl = "https://newsapi.org/v2/"

def handle_request(url):
    url = f'{baseurl}{url}&apiKey={apiKey}'
    response_API = requests.get(url)
    data = response_API.text
    parse_json = json.loads(data)
    return parse_json

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
    newes=handle_request("everything?q=country=in")["articles"]
    return render_template("index.html",newes=newes,categorys=categorys)

@app.route(f'/category/<cats>')
def category(cats):
    if(cats.lower() in categorys):
        newes=handle_request("everything?q=country=in")["sources"]
        return render_template('category.html',newes=newes,cats=cats,categorys=categorys)
    else:
        return "Not Found"

if __name__ == '__main__':
    app.run(debug=True)