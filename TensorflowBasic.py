import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as te

#Normal Distribution
x = te.random.normal((4,4), mean=0, stddev=1)
print("Normal Distribution")
print(x)

#uniform distribution
x = te.random.uniform((1,5), minval=0, maxval=2)
print("Uniform Distribution")
print(x)