import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as te

print(te.__version__)

#tensor
tensorA = te.constant(8)
print(tensorA)