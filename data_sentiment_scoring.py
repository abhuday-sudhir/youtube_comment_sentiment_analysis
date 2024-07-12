import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def get_sentiment_scores(df,comments):
    analyzer=SentimentIntensityAnalyzer()
    positive_scores = []
    negative_scores = []
    neutral_scores=[]
    for comment in comments:
        info=[]
        scores = analyzer.polarity_scores(comment)
        sentiment_score = scores['compound']
        info.append(sentiment_score)
        if sentiment_score >=0.05:
            positive_scores.append(sentiment_score)
            info.append("positive")
        elif sentiment_score <= -0.05:
            negative_scores.append(sentiment_score)
            info.append("negative")
        else :
            neutral_scores.append(sentiment_score)
            info.append("neutral")
        df.loc[len(df)]= info

    return df,positive_scores,neutral_scores, negative_scores