import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as te

#Normal Distribution
x = te.random.normal((4,4), mean=0, stddev=1)
print("Normal Distribution")
print(x)