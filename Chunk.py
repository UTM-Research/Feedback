import nltk
words=nltk.word_tokenize('Text Data')
print(words)
tagged=nltk.pos_tag(words)
print(tagged)
new_gram_np=r"NP:{<DT>? <NN>*<NN>|<NN>*<NNS>}"
parser=nltk.RegexpParser(new_gram_np)
chunked=parser.parse(tagged)
print(chunked)
chunked.draw()
lines = 'lines is some string of words'
# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN'
# do the nlp stuff
tokenized = nltk.word_tokenize(lines)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
print(nouns)
