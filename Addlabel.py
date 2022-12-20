import matplotlib.pyplot as plt
import networkx as nx
import nltk
import networkx as nx
from collections import Counter
def adlab(listnode, val):
    G = nx.Graph()
    counts = Counter(listnode)
    for row in listnode:
        wx1 = val
        wx2 = row
        G.add_edge(wx1, wx2)
    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G,pos,edge_color='black',width=1,linewidths=1, node_size=500,node_color='pink',alpha=0.9, labels={node:node for node in G.nodes()})
    for itm in listnode:
        lab=counts[itm]
        nx.draw_networkx_edge_labels(G,pos,edge_labels={(val,itm):lab},font_color='blue')
    plt.axis('off')
    plt.show()