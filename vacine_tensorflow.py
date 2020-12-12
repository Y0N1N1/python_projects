# -*- coding: utf-8 -*-
"""vaccine_effect
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1mGXRvU43gbttCYpjBOfVDStqfohx1-lU
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x #this project was made on google colaboratory, so you wont need to install this if you are on anywhere else.
import numpy as np
from random import randint
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy



train_labels = []
train_samples = []



for i in range(50):
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(1)

    random_older = randint(65,100)
    train_samples.append(random_older)
    train_labels.append(0)

for i in range(1000):
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(0)

    random_older = randint(65,100)
    train_samples.append(random_older)
    train_labels.append(1)



train_labels = np.array(train_labels)
train_samples = np.array(train_samples)
train_labels, train_samples = shuffle(train_labels, train_samples)

scale = MinMaxScaler(feature_range=(0,1))
scale_train_samples = scale.fit_transform(train_samples.reshape(-1,1))

def see_dataset():
    for i in scale_train_samples, train_labels:
        print(i)



model = Sequential([
    Dense(units=16, input_shape=(1,), activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=2, activation='softmax')
])

def see_model():
    model.summary()



model.compile(optimizer=Adam(learning_rate=0.1), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x=scale_train_samples, y=train_labels, batch_size=10, epochs=15, shuffle=True, verbose=2)

'''
--Dummy data vaccine effect--
I made some fake data where 95% of people between 13-65 years old have no effect from a fake vaccine, and only 5% has.
Then I did the opposite of old people. I then turned my data into NumPy, gave it to a NN with 3 layers: relu, relu and softmax, 
then messed around with the epochs and learning rate to see what happens. 
I started with 0.0001 learning rate and 30 epochs. I then decreased the epochs to 15 and increased the learning rate to 0.1, 
where I found an almost perfect result (93-94%) and I tried to increase the learning rate, or decrease the epochs, but I only got worse results. 
These are the optimal levels for my data samples. 
--end--
'''