import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as te
import keras
from keras import layers
from keras.datasets import mnist

(x_train, y_train) , (x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(y_train.shape)



