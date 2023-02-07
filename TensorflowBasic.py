import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as te

# #Normal Distribution
# x = te.random.normal((4,4), mean=0, stddev=1)
# print("Normal Distribution")
# print(x)

# #uniform distribution
# x = te.random.uniform((1,5), minval=0, maxval=2)
# print("Uniform Distribution")
# print(x)

# #range function
# x = te.range(start=5, limit=20, delta=3)
# print("Range function")
# print(x)

# #casting
# y = te.cast(x, dtype=te.float64)
# print("Casting")
# print(y)

# #element wise addition
# tensorA = te.constant([20,6,7])
# tensorB = te.constant([45,7,21])

# print(tensorA)
# print(tensorB)

# print ("Tensor Addition")
# #tensorC = te.add(tensorA, tensorB)
# tensorC = tensorA + tensorB
# print(tensorC)

# #tensor subtraction
# print("Tensor Subtraction")
# tensorC = tensorA - tensorB
# print(tensorC)

# #tensorflow division
# print("Tensor devision")
# tensorC = te.divide(tensorA,tensorB)
# print(tensorC)

# #tensor multiplication
# print("Tensor multiplication")
# tensorC = te.multiply(tensorA, tensorB)
# print(tensorC)

print("Dot Product")
import numpy as np

tensorA = te.constant(np.array([[1,2],[3,4]]))
tensorB = te.constant(np.array([[11,12],[13,14]]))

print("tensorA")
print(tensorA)

print("tensorB")
print(tensorB)

#[[1*11 + 2*13]] ....

print("Dot Product")
tensorC = te.tensordot(tensorA, tensorB, axes=1)
print(tensorC)