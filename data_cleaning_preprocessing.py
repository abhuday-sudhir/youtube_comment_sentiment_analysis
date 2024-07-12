import pandas as pd
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re

porter=PorterStemmer()

def stemming_words(text):
    review=text.split()
    review=[porter.stem(word) for word in review]
    review=" ".join(review)
    print(review)
    return review


def cleaning_preprocessing(comments):
    data=pd.DataFrame(comments,columns=['comments'])

    data['comments']=data['comments'].apply(lambda x:re.sub('[^a-z A-Z 0-9-]','',x))
    #lowering case
    data['comments']=data['comments'].apply(lambda x:x.lower())
    #Removing stopwords
    data['comments']=data['comments'].apply(lambda x:' '.join([y for y in x.split() if y not in stopwords.words('english')]))
    #Removing url
    data['comments']=data['comments'].apply(lambda x: re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , str(x)))
    #Removing html tags
    data['comments']=data['comments'].apply(lambda x: BeautifulSoup(x,"lxml").get_text())
    #Removng extra spaces
    data['comments']=data['comments'].apply(lambda x:" ".join(x.split()))
    #Performing lemmatization
    data['comments']=data['comments'].apply(lambda x: stemming_words(x))

    comments_cleaned=data['comments'].tolist()

    return comments_cleaned