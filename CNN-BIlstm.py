from keras.preprocessing.text import one_hot
from keras.layers import Dense, LSTM, Bidirectional
from keras.layers import TimeDistributed
from numpy import array
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers import LSTM
# define documents
docs = ["Add you Documents, X"]
# define class labels
labels = array(["Add class label, Y"])
# integer encode the documents
vocab_size = 50
encoded_docs = [one_hot(d, vocab_size) for d in docs]
print(encoded_docs)
# pad documents to a max length of 4 words
max_length = 4
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
print(padded_docs)
# define the model
model = Sequential()
model.add(Embedding(vocab_size, 64, input_length=max_length))
model.add(Conv1D(filters=12, kernel_size=2, activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(TimeDistributed(Flatten()))
model.add(Bidirectional(LSTM(50, activation='relu')))
model.add(Dense(1, activation='sigmoid'))
print(model.summary())
# compile network
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit network
model.fit(padded_docs, labels, epochs=10, verbose=2)
# evaluate
loss, acc = model.evaluate(padded_docs, labels, verbose=0)
print('Test Accuracy: %f' % (acc*100))