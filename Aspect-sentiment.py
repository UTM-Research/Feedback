import nltk
from nltk.corpus import stopwords
txt = "The Sound Quality is great but the battery life is very bad."
txt = txt.lower()
sentList = nltk.sent_tokenize(txt)
for line in sentList:
    txt_list = nltk.word_tokenize(line)
    taggedList = nltk.pos_tag(txt_list)
print(taggedList)
newwordList = []
flag = 0
for i in range(0,len(taggedList)-1):
    if(taggedList[i][1]=="NN" and taggedList[i+1][1]=="NN"):
        newwordList.append(taggedList[i][0]+taggedList[i+1][0])
        flag=1
    else:
        if(flag==1):
            flag=0
            continue
        newwordList.append(taggedList[i][0])
        if(i==len(taggedList)-2):
            newwordList.append(taggedList[i+1][0])
finaltxt = ' '.join(word for word in newwordList)
print(finaltxt)
stop_words = set(stopwords.words('english'))
new_txt_list = nltk.word_tokenize(finaltxt)
wordsList = [w for w in new_txt_list if not w in stop_words]
taggedList = nltk.pos_tag(wordsList)
print(taggedList)
dep_parser = nltk.CoreNLPDependencyParser(url='http://localhost:9000')
nltk.parse.corenlp.GenericCoreNLPParser(url='http://localhost:9000', encoding='utf8', tagtype=None)
parse, = dep_parser.raw_parse('The quick brown fox jumps over the lazy dog.')
print(parse.to_conll(4))