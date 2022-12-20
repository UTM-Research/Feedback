import spacy
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from csv import DictReader
import Barchart
import nltk
from nltk.stem import PorterStemmer, porter
porter = PorterStemmer()
from nltk.stem import LancasterStemmer
lancaster=LancasterStemmer()
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
allwordtag=[]
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
from colorama import Fore
from colorama import Style
nlp = spacy.load("en_core_web_sm")
allpos=[]
allneg=[]
allneu=[]
pos=0
neg=0
neu=0
def readfdic(asl):
    sent=0
    with open("D:\\1---Sedraya--FEEDBACK\\1-Second paper- bothe aspect & general\\dataset-For- second paper\\1-related\\dictionary.csv", 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            if row['word']==asl:
                sent=row['val']
    read_obj.close()
    if not sent:
        sent=0
        return sent
    else:
        return sent
def root(txt):
    sent1 = 0
    text_data1 = txt
    text_data = nltk.word_tokenize(text_data1)
    taggedList = nltk.pos_tag(text_data)
    lemmatizer = WordNetLemmatizer()
    allwordtag = []
    word1 = []
    for k in taggedList:
        if (k[1] == 'VERB' or k[1] == 'VBD' or k[1] == 'VB' or k[1] == 'VBG' or k[1] == 'VBN' or k[1] == 'VBP' or k[
            1] == 'VBZ' or k[1] == 'VRB' or k[1] == 'ADV' or k[1] == 'ADJ' or k[1] == 'JJ' or k[1] == 'NN' or k[
            1] == 'JJR' or k[1] == 'JJS' or k[1] == 'NNPS' or k[1] == 'NNP' or k[1] == 'NNS' or k[1] == 'RBR' or k[
            1] == 'RBS' or k[1] == 'RB' or k[1] == 'IN'):
            if not (k[0] == ',' or k[0] == '’' or k[0] == '’' or k[0] == 'e.g' or k[0] == 'E.g'):
                if k[1] in ('VB', 'VBD', 'VERB', 'VB', 'VBG', 'VBN', 'VBP', 'VBZ', 'VRB'):
                    pas = 'v'
                if k[1] in ('IN'):
                    pas = 'v'
                elif k[1] in ('NN', 'NNS', 'NNP', 'NNPS'):
                    pas = 'n'
                elif k[1] in ('ADJ', 'JJ', 'JJR', 'JJS'):
                    pas = 'a'
                elif k[1] in ('ADV', 'RB', 'RBR', 'RBS'):
                    pas = 'r'
                org=lemmatizer.lemmatize(k[0], pos=pas)
                mid=readfdic(org)
                allwordtag.append({'POS': pas, 'scor': mid, 'word': org})
                #aspect = TextBlob(org).sentiment

                if  (k[1] in ('ADV', 'RB', 'RBR', 'RBS')) and (k[0] in ('no', 'NOT', 'not', 'don', "n't", 'won')):
                    mid=mid * (-1)
                    sent1 = float(mid) + float(sent1)
                else:
                    sent1 = float(mid) + float(sent1)
    import polcalc
    sent1=polcalc.calc(allwordtag)
    return sent1
with open("YOUR TEXT DATA PATH") as f:

    for line in f:
        txt = line.lower()
        sentList = nltk.sent_tokenize(txt)
        for v in sentList:
            asl=root(v)
            sia = SentimentIntensityAnalyzer()
            s = sia.polarity_scores(v)
            aspect = TextBlob(v).sentiment
            if asl<0 and s['compound']<0:
                allneg.append({'sen': v, 'sentiment_score': s['compound']})
                neg = neg - 1
            elif asl==0 and s['compound']==0:
                 allneu.append({'sen': v, 'sentiment_score': s['compound']})
                 neu = neu + 1
            elif asl > 0 and s['compound'] > 0:
                allpos.append({'sen': v, 'sentiment_score': s['compound']})
                pos = pos + 1
            elif asl >= 0 and s['compound'] < 0:
                allneg.append({'sen': v, 'sentiment_score': s['compound']})
                neg = neg - 1
            elif asl < 0 and s['compound'] >= 0:
                allneg.append({'sen': v, 'sentiment_score': asl})

                neg = neg - 1

barchart.shape(pos, neg)
input("Press any key to continue")

print("============================================= Negative Students Feedback ======================================")
for we in allneg:
    exp = we['sen']
    sco = str(we['sentiment_score'])
    print(Fore.BLUE + 'Student\'s Comment:' + Style.RESET_ALL + exp, '          ', '\n', Fore.RED + 'Sentiment score:' + Style.RESET_ALL + sco)
print('\n')
print("============================================= Positive Students Feedback ======================================")
for we in allpos:
    exp = we['sen']
    sco = str(we['sentiment_score'])
    print(Fore.BLUE + 'Student\'s Comment:' + Style.RESET_ALL + exp, '          ', '\n', Fore.RED + 'Sentiment score:' + Style.RESET_ALL + sco)

print('\n')
print("============================================= Neutral Students Feedback ======================================")
for we in allneu:
    exp = we['sen']
    sco = str(we['sentiment_score'])
    print(Fore.BLUE + 'Student\'s Comment:' + Style.RESET_ALL + exp, '          ', '\n',  Fore.RED + 'Sentiment score:' + Style.RESET_ALL + sco)
   print('\n', '\n')

import summarize
v=input("DO YOU WANT TO CREATE A SUMMARY OF STUDENTS FEEDBACK (Y/N):")
print('\n')
v=v.lower()
if v=='y':
    summarize.summary(allneg, 1)
    summarize.summary(allpos, 2)
    summarize.summary(allneu, 3)