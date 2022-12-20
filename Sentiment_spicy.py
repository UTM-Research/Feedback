import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
print(spacy.explain('PROPN'))
sentences = ['Text Data']
for sentence in sentences:
  doc = nlp(sentence)
  for token in doc:
    print(token.text, '   ', token.pos_, token.dep_, ' ', [child for child in token.children])
aspects = []
for sentence in sentences:
  doc = nlp(sentence)
  descriptive_term = ''
  target = ''
  for token in doc:
    if token.dep_ == 'nsubj' and token.pos_ == 'NOUN':
      target = token.text
    if token.pos_ == 'ADJ':
      prepend = ''
      for child in token.children:
        if child.pos_ != 'ADV':
          continue
        prepend += child.text + ' '
      descriptive_term = prepend + token.text
  aspects.append({'aspect': target,
    'description': descriptive_term})
print(aspects)