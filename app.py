from flask import Flask,render_template,request,jsonify,url_for
from urllib import parse
from googleapiclient.discovery import build
from data_collection import video_comments
from data_cleaning_preprocessing import cleaning_preprocessing
from data_sentiment_scoring import get_sentiment_scores
import pandas as pd

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/analysis",methods=['POST'])
def analysis():
    video_url=request.form['video_url']
    parsed_url=parse.urlparse(video_url)
    video_id = parse.parse_qs(parsed_url.query)['v'][0]
    comments=video_comments(video_id)
    clean_comments=cleaning_preprocessing(comments)
    df,positive_scores,neutral_scores, negative_scores=get_sentiment_scores(pd.DataFrame(columns=['Sentiment_Score','Nature of comment']),clean_comments)
    df.insert(0,column="Comments",value=comments)

    return render_template('analysis.html', df=df.to_html())


if __name__=="__main__":
    app.run(debug=True,port=5000)