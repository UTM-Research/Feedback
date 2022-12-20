from pandas import read_csv
from matplotlib import pyplot
dataframe = read_csv(url, header=None)

print(dataframe.shape)

print(dataframe.head())

from pandas import read_csv
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

dataframe = read_csv(url, header=None)
dataset = dataframe.values

X, y = dataset[:, 1:-1], dataset[:, -1]
X, y = X.astype('float'), y.astype('float')
n_features = X.shape[1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

model = Sequential()
model.add(Dense(20, input_dim=n_features, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(10, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mse', optimizer='adam')

model.fit(X_train, y_train, epochs=150, batch_size=32, verbose=2)

yhat = model.predict(X_test)
error = mean_absolute_error(y_test, yhat)
print('MAE: %.3f' % error)