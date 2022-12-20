from nltk.corpus import stopwords
import nltk
from nltk.stem import PorterStemmer, porter
porter = PorterStemmer()
from nltk.stem import LancasterStemmer
lancaster=LancasterStemmer()
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
word1=[]
val = input("Enter your value: ")
with open("C:\\1---Sedraya--FEEDBACK\\1-Second paper- bothe aspect & general\\dataset-For- second paper\\1-related\\textdata.txt") as f:
    for line in f:
        txt = line.lower()
        sentList = nltk.sent_tokenize(txt)
        stop_words = set(stopwords.words('english'))
        for line in sentList:
            if val in line:
                txt_list = nltk.word_tokenize(line)
                taggedList = nltk.pos_tag(txt_list)
                for k in taggedList:
                    if k[1] in ('NN', 'NNS', 'NNP', 'NNPS'):
                        if not (k[0] == ',' or k[0] == '’' or k[0] == '’' or k[0] == 'e.g' or k[0] == 'E.g'):
                            word1.append(k[0])
import figconcept
figconcept. shape(word1, val)