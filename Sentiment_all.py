import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
sentences = ['']
for sentence in sentences:
  doc = nlp(sentence)
  for token in doc:
    print(token.text, '   ', token.dep_, '  ')