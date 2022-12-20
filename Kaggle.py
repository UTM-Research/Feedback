import pandas as pd
import re
import spacy
nlp = spacy.load("en_core_web_sm")
from tqdm import tqdm

toy_rev = pd.read_csv("Text Data",engine='python',index_col=False)
toy_rev.head()
toy_rev['review']=toy_rev['teaching']
aspect_terms = []
comp_terms = []
easpect_terms = []
ecomp_terms = []
enemy = []
for x in tqdm(range(len(toy_rev['review']))):
    amod_pairs = []
    advmod_pairs = []
    compound_pairs = []
    xcomp_pairs = []
    neg_pairs = []
    eamod_pairs = []
    eadvmod_pairs = []
    ecompound_pairs = []
    eneg_pairs = []
    excomp_pairs = []
    enemlist = []
    if len(str(toy_rev['review'][x])) != 0:
        lines = str(toy_rev['review'][x]).replace('*', ' ').replace('-', ' ').replace('so ', ' ').replace('be ',
                                                                                                          ' ').replace(
            'are ', ' ').replace('just ', ' ').replace('get ', '').replace('were ', ' ').replace('When ', '').replace(
            'when ', '').replace('again ', ' ').replace('where ', '').replace('how ', ' ').replace('has ', ' ').replace(
            'Here ', ' ').replace('here ', ' ').replace('now ', ' ').replace('see ', ' ').replace('why ', ' ').split(
            '.')
        for line in lines:
            enem_list = []
            for eny in competitors:
                enem = re.search(eny, line)
                if enem is not None:
                    enem_list.append(enem.group())
            if len(enem_list) == 0:

                doc = nlp(line)
                str1 = ''
                str2 = ''
                for token in doc:
                    if token.pos_ is 'NOUN':
                        for j in token.lefts:
                            if j.dep_ == 'compound':
                                compound_pairs.append((j.text + ' ' + token.text, token.text))
                            if j.dep_ is 'amod' and j.pos_ is 'ADJ':  # primary condition
                                str1 = j.text + ' ' + token.text
                                amod_pairs.append(j.text + ' ' + token.text)
                                for k in j.lefts:
                                    if k.dep_ is 'advmod':  # secondary condition to get adjective of adjectives
                                        str2 = k.text + ' ' + j.text + ' ' + token.text
                                        amod_pairs.append(k.text + ' ' + j.text + ' ' + token.text)
                                mtch = re.search(re.escape(str1), re.escape(str2))
                                if mtch is not None:
                                    amod_pairs.remove(str1)
                    if token.pos_ is 'VERB':
                        for j in token.lefts:
                            if j.dep_ is 'advmod' and j.pos_ is 'ADV':
                                advmod_pairs.append(j.text + ' ' + token.text)
                            if j.dep_ is 'neg' and j.pos_ is 'ADV':
                                neg_pairs.append(j.text + ' ' + token.text)
                        for j in token.rights:
                            if j.dep_ is 'advmod' and j.pos_ is 'ADV':
                                advmod_pairs.append(token.text + ' ' + j.text)
                    if token.pos_ is 'ADJ':
                        for j, h in zip(token.rights, token.lefts):
                            if j.dep_ is 'xcomp' and h.dep_ is not 'neg':
                                for k in j.lefts:
                                    if k.dep_ is 'aux':
                                        xcomp_pairs.append(token.text + ' ' + k.text + ' ' + j.text)
                            elif j.dep_ is 'xcomp' and h.dep_ is 'neg':
                                if k.dep_ is 'aux':
                                    neg_pairs.append(h.text + ' ' + token.text + ' ' + k.text + ' ' + j.text)

            else:
                enemlist.append(enem_list)
                doc = nlp(line)
                str1 = ''
                str2 = ''
                for token in doc:
                    if token.pos_ is 'NOUN':
                        for j in token.lefts:
                            if j.dep_ == 'compound':
                                ecompound_pairs.append((j.text + ' ' + token.text, token.text))
                            if j.dep_ is 'amod' and j.pos_ is 'ADJ':  # primary condition
                                str1 = j.text + ' ' + token.text
                                eamod_pairs.append(j.text + ' ' + token.text)
                                for k in j.lefts:
                                    if k.dep_ is 'advmod':  # secondary condition to get adjective of adjectives
                                        str2 = k.text + ' ' + j.text + ' ' + token.text
                                        eamod_pairs.append(k.text + ' ' + j.text + ' ' + token.text)
                                mtch = re.search(re.escape(str1), re.escape(str2))
                                if mtch is not None:
                                    eamod_pairs.remove(str1)
                    if token.pos_ is 'VERB':
                        for j in token.lefts:
                            if j.dep_ is 'advmod' and j.pos_ is 'ADV':
                                eadvmod_pairs.append(j.text + ' ' + token.text)
                            if j.dep_ is 'neg' and j.pos_ is 'ADV':
                                eneg_pairs.append(j.text + ' ' + token.text)
                        for j in token.rights:
                            if j.dep_ is 'advmod' and j.pos_ is 'ADV':
                                eadvmod_pairs.append(token.text + ' ' + j.text)
                    if token.pos_ is 'ADJ':
                        for j in token.rights:
                            if j.dep_ is 'xcomp':
                                for k in j.lefts:
                                    if k.dep_ is 'aux':
                                        excomp_pairs.append(token.text + ' ' + k.text + ' ' + j.text)
        pairs = list(set(amod_pairs + advmod_pairs + neg_pairs + xcomp_pairs))
        epairs = list(set(eamod_pairs + eadvmod_pairs + eneg_pairs + excomp_pairs))
        for i in range(len(pairs)):
            if len(compound_pairs) != 0:
                for comp in compound_pairs:
                    mtch = re.search(re.escape(comp[1]), re.escape(pairs[i]))
                    if mtch is not None:
                        pairs[i] = pairs[i].replace(mtch.group(), comp[0])
        for i in range(len(epairs)):
            if len(ecompound_pairs) != 0:
                for comp in ecompound_pairs:
                    mtch = re.search(re.escape(comp[1]), re.escape(epairs[i]))
                    if mtch is not None:
                        epairs[i] = epairs[i].replace(mtch.group(), comp[0])

    aspect_terms.append(pairs)
    comp_terms.append(compound_pairs)
    easpect_terms.append(epairs)
    ecomp_terms.append(ecompound_pairs)
    enemy.append(enemlist)
toy_rev['compound_nouns'] = comp_terms
toy_rev['aspect_keywords'] = aspect_terms
toy_rev['competition'] = enemy
toy_rev['competition_comp_nouns'] = ecomp_terms
toy_rev['competition_aspects'] = easpect_terms
toy_rev.head()

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


import operator
sentiment = []
for i in range(len(toy_rev)):
    score_dict={'pos':0,'neg':0,'neu':0}
    if len(toy_rev['aspect_keywords'][i])!=0:
        for aspects in toy_rev['aspect_keywords'][i]:
            sent = analyser.polarity_scores(aspects)
            score_dict['neg'] += sent['neg']
            score_dict['pos'] += sent['pos']
        sentiment.append(max(score_dict.items(), key=operator.itemgetter(1))[0])
    else:
        sentiment.append('NaN')
toy_rev['sentiment'] = sentiment
toy_rev.head()

int_sent = []
for sent in toy_rev['sentiment']:
    if sent is 'NaN':
        int_sent.append('NaN')
    elif sent is 'pos':
        int_sent.append('1')
    else:
        int_sent.append('0')
toy_rev['int_sent'] = int_sent
toy_rev.head()

import math
pos = []
for i in range(len(toy_rev)):
    if not math.isnan(toy_rev['Rating'][i]):
        if int(toy_rev['Rating'][i])>0:
            pos.append('1')
        else:
            pos.append('0')
    else:
        pos.append('0')
toy_rev['Positive Review'] = pos
toy_rev.head()

d = {'sent':toy_rev['Positive Review'],'sent_pred':toy_rev['int_sent']}
metric_df = pd.DataFrame(data=d)
metric_df.head()

metric_df = metric_df[metric_df.sent_pred != 'NaN']
len(metric_df.sent)

from sklearn.metrics import accuracy_score,auc,f1_score,recall_score,precision_score
print('accuracy')
print(accuracy_score(metric_df.sent, metric_df.sent_pred))
print('f1 score')
print(f1_score(metric_df.sent, metric_df.sent_pred,pos_label='1'))
print('recall')
print(recall_score(metric_df.sent, metric_df.sent_pred,pos_label='1'))
print('precision')
print(precision_score(metric_df.sent, metric_df.sent_pred,pos_label='1'))