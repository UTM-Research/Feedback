import networkx as nx
import pylab as plt
import nltk
G=nx.Graph()
# Add nodes and edges
def shape (points, val):
    for row in points:
        wx1=val
        wx2=row
        G.add_edge(wx1, wx2)

    nx.draw(G, with_labels = True)
    plt.axis("off")
    plt.show()
    val1 = input("Enter your value to show corresponding sentences: ")
    ind=1
    with open("Text data") as f:
        for line in f:
            txt = line.lower()
            sentList = nltk.sent_tokenize(txt)
            for line in sentList:
                if (val1 in line) and (val in line):
                    print(str(ind) +'-'+line)
                    ind=ind+1

    input("Press any key to continue")