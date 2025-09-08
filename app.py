
from flask import Flask, render_template,request,redirect,url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client["SIH_DB"]


@app.route('/ministries.html',methods = ["GET","POST"])
def ministries():
    
    return render_template('ministries.html')

@app.route('/submit',methods = ["POST"])
def submit():
    ministry = request.form.get("ministry")
    sentiment = request.form.get("sentiment")

    print(ministry,sentiment)

    return redirect(url_for("news_titles", ministry=ministry, sentiment=sentiment))

@app.route('/news_titles.html')
def news_titles():
    ministry = request.args.get("ministry")
    sentiment = request.args.get("sentiment")

    print(ministry,sentiment)
    news_data = []
    alltitles = db.Processed_News.find()

    for objects in alltitles:
        if objects['Ministries'] == ministry and objects['Sentiment'] == sentiment:
            news_data.append({'title':objects['title'],'Sentiment':objects['Sentiment']})
    
    return render_template('news_titles.html',news_data = news_data)


@app.route('/')

def homepage():

    return render_template('homepage.html')





