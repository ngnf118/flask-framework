import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.models import Model
from keras.layers import Dense, LSTM, Activation
from keras.layers import Input

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

from datetime import datetime
import pytz
import matplotlib.pyplot as plt

def create_dataset(dataset, look_back=1):

    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        dataX.append(dataset[i:(i+look_back),0])
        dataY.append(dataset[i+look_back,0])
    return np.array(dataX), np.array(dataY)

if __name__ == "__main__":


    # load data
    data = pd.read_csv("occurrence_by_year.csv")
    # data = pd.read_csv("database.csv")
    scaler = MinMaxScaler(feature_range=(0, 1))


    look_back_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    column_names = ['occurrence']
    # column_names = ['Depth', 'Magnitude', 'Latitude', 'Longitude', 'Date', 'Time']


    for col in column_names:
        for j in look_back_list:

            dataset = np.array(data[col].values).reshape(-1, 1)
            dataset = dataset.astype('float32')
            dataset = scaler.fit_transform(dataset)

            # split into train and test sets
            train_size = int(len(dataset) * 0.7)
            test_size = int(len(dataset) * 0.3)
            train, test = dataset[0:train_size, :], dataset[train_size:(train_size+test_size), :]

            # reshape for look_back
            look_back = j
            X_train, y_train = create_dataset(train, look_back)
            X_test, y_test = create_dataset(test, look_back)


            # reshape for LSTM [samples, time steps, features]
            X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
            X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))


            # LSTM
            model = Sequential()
            model.add(LSTM(500, input_dim=1))
            # model.add(Dense(16))
            # model.add(Activation('relu'))
            # model.add(Dense(4))
            # model.add(Activation('relu'))
            model.add(Dense(1))

            model.compile(loss='mean_squared_error', optimizer='adam')
            model.fit(X_train, y_train, nb_epoch=500, batch_size=20, verbose=2)

            train_pred = model.predict(X_train)
            test_pred = model.predict(X_test)

            # scale back
            train_pred = scaler.inverse_transform(train_pred)
            y_train = np.array(y_train).reshape(1, -1)
            y_train = scaler.inverse_transform(y_train)
            test_pred = scaler.inverse_transform(test_pred)
            y_test = np.array(y_test).reshape(1, -1)
            y_test = scaler.inverse_transform(y_test)

            # shift predictions for plotting
            train_pred_plot = np.empty_like(dataset)
            train_pred_plot[:, :] = np.nan
            train_pred_plot[look_back:len(train_pred) + look_back, :] = train_pred

            test_pred_plot = np.empty_like(dataset)
            test_pred_plot[:, :] = np.nan
            test_pred_plot[len(train_pred) + (look_back * 2) + 1:train_size + test_size - 1, :] = test_pred

            f = plt.figure()
            plt.plot(scaler.inverse_transform(dataset[0:train_size + test_size]), color='b', lw=2.0, label=''+col+'-lookback-'+str(j))
            plt.plot(train_pred_plot, color='g', lw=2.0, label='LSTM train')
            plt.plot(test_pred_plot, color='r', lw=2.0, label='LSTM test')
            plt.legend(loc=3)
            plt.grid(True)
            f.savefig('q3_plots/LSTM-'+col+'-lookback-'+str(j)+'.png')

            print(col)
            print(j)




