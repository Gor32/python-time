import numpy as np

##C = [[1,2,3],
##     [0,4,5],
##     [0,0,6]]
##print(C)
##
##U = np.array(C)
##print(U)
##
##print(U.T)
##
##A = U.T.dot(U)
##print(A)
##
##print(A.trace())

import pandas as pd
import matplotlib.pyplot as plt

def run_regression(data, response):
  X = np.array([[1, x] for x in data])
  Y = np.array(response)
  beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
  return beta

df = pd.read_csv("train.csv")
b0, b1 = run_regression(list(df['x']), list(df['y']))
line_x = np.arange(0, 100,1)
line_y = [b0 + b1 * x for x in line_x]
plt.clf()  
plt.scatter(df['x'], df['y'], s=3, color='cyan')
plt.plot(line_x, line_y, color='red')
plt.savefig("regression0.png", dpi=160)


