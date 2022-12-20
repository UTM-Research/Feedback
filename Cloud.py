import networkx as nx
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
G=nx.Graph()
comment_words = ''
with open("Text Data") as f:
    for line in f:

        stopwords = set(STOPWORDS)

        val = str(line)

    # split the value
        tokens = val.split()

    # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        comment_words += " ".join(tokens) + " "

    wordcloud = WordCloud(width=1000, height=1000, background_color='white',
                      stopwords=stopwords, max_words=2500, min_font_size=10).generate(comment_words)

    # plot the WordCloud image
    plt.figure(figsize=(10, 10), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
    new_tokens = word_tokenize(comment_words)
    new_tokens = [t.lower() for t in new_tokens]
    new_tokens = [t for t in new_tokens if t not in stopwords]
    new_tokens = [t for t in new_tokens if t.isalpha()]
    lemmatizer = nltk.WordNetLemmatizer()
    new_tokens = [lemmatizer.lemmatize(t) for t in new_tokens]
    from nltk import ngrams, FreqDist

# term frequency:
    all_counts = dict()
    for size in 1, 2, 3, 4, 5:
        all_counts[size] = FreqDist(ngrams(new_tokens, size))
    list=all_counts[1].most_common()
word2=[]
flag=1
while (flag==1):
    for r in list:
        x1=str(r[0])
        x1=x1.replace('(', '')
        x1 = x1.replace(',)', '')
        x2=str(r[1])
        print(x1,'=', x2)
    print("\n")
    val = input("Enter your value (word) for the concept mapping: ")
    val=val.lower()
    print("\n")
    with open("D:\\1---Sedraya--FEEDBACK\\1-Second paper- bothe aspect & general\\dataset-For- second paper\\1-related\\textdata.txt") as f:
        for line in f:
            txt = line.lower()
            sentList = nltk.sent_tokenize(txt)

            for line in sentList:
                if val in line:
                    txt_list = nltk.word_tokenize(line)
                    taggedList = nltk.pos_tag(txt_list)
                    for k in taggedList:
                        if k[1] in ('NN', 'NNS', 'NNP', 'NNPS'):
                            if not (k[0] == ',' or k[0] == '’' or k[0] == '’' or k[0] == 'e.g' or k[0] == 'E.g' or k[0] == 'i' or k[0] == 'I'):
                                word2.append(k[0])
#-------------------------------------------------------
    import Addlabel
    addlable.adlab(word2, val)
#----------------------------------------------------
    val1 = input("Enter your value (word) to show corresponding sentences: ")
    val1=val1.lower()
    print("\n")
    ind = 1
    with open("Text Data") as f:
        for line in f:
            txt = line.lower()
            sentList = nltk.sent_tokenize(txt)
            for line in sentList:
                if (val1 in line) and (val in line):
                    print(str(ind) + '-' + line)
                    print("\n")
                    ind = ind + 1
    word2 = []
    val=''
    val1=''
    G = nx.Graph()
    flag=input("To stop current process (press '0').  T o continue press any key to continue:")

    if flag!=str(0):
        flag=1
    elif flag==str(0):
      flag=0
