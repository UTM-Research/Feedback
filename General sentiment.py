from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
text = "Text Data"
obj = TextBlob(text)
sentiment = obj.sentiment.polarity
print(sentiment)
sia = SentimentIntensityAnalyzer()
s=sia.polarity_scores("Text Data")
print(s)
analyser = SentimentIntensityAnalyzer()
sent = analyser.polarity_scores(text)
print(sent['pos'])