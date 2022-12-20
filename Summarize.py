import nltk
nltk.download()
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stopwords=set(stopwords.words("english"))
def summary(txt, con):
    fulltxt = ''
    for sentence  in txt:
        fulltxt +=" " + sentence['sen']
    words=word_tokenize(fulltxt)
    freqtable=dict()
    for word in words:
        word=word.lower()
        if word in stopwords:
            continue
        if word in freqtable:
            freqtable[word]+=1
        else:
            freqtable[word]=1
    sentences=sent_tokenize(fulltxt)
    sentencevalue=dict()

    for sentence in sentences:
        for word, freq in freqtable.items():
            if word in sentence.lower():
                if sentence in sentencevalue:
                    sentencevalue[sentence] += freq
                else:
                    sentencevalue[sentence]= freq
    sumvalue=0
    summary1=''
    if len(sentencevalue)>0:
        for sentence in sentencevalue:
            sumvalue +=sentencevalue[sentence]
        average=int(sumvalue/len(sentencevalue))
        summary1=''
        for sentence  in sentences:
            if (sentence in sentencevalue) and (sentencevalue[sentence] >(1.2 *average)):
                summary1 +=" " + sentence
    if con==1:
        print("============================================= [Summary of Negative Students Feedback] =======================================")
        sentences=sent_tokenize(summary1)
        for sen in sentences:
            print(sen, '\n')

    if con == 2:
        print("============================================= [Summary of Positive Students Feedback] =======================================")
        sentences = sent_tokenize(summary1)
        for sen in sentences:
            print(sen, '\n')

    if con == 3:
        print("============================================= [Summary of Neutral Students Feedback] =======================================")
        sentences = sent_tokenize(summary1)
        for sen in sentences:
            print(sen, '\n')
