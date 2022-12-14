# # -*- coding: utf-8 -*-
# """MR2Framework.ipynb

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/1Xl9IE92v3Flp2uyRg_jqpfqIQyr4_SaQ
# """

# from google.colab import drive

# drive.mount("/content/gdrive")  
# !pwd  # show current path

# # Commented out IPython magic to ensure Python compatibility.
# # %cd "/content/gdrive/MyDrive/ClasesMachineLearning"
# !ls  # show current directory

import numpy as np
from random import randrange
import matplotlib.pyplot as plt
import math
import pandas as pd
import seaborn as sn

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV

from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor, HistGradientBoostingRegressor, RandomForestClassifier
from sklearn.svm import SVR, NuSVR
from sklearn.gaussian_process import GaussianProcessRegressor

df = pd.read_csv('fifa_eda_stats.csv')
#df = pd.read_csv('wine.data')
df.head(1)

def transform(value):
  aux=None
  if (type(value)==str):
    value = value.replace("€","")
    if ("M" in value):
      aux = (value.replace("M",""))
      aux=float(aux)*1000
    if ("K" in value):
      aux = (value.replace("K",""))
      aux=float(aux)*1
  else:
    aux=value
  return aux

df = pd.read_csv('fifa_eda_stats.csv')
#df = pd.read_csv('wine.data')
df.head(1)
df = df.drop(["Name","Club","Nationality","ID","Work Rate","Body Type","Position","Position","Jersey Number","Joined"],axis=1)
df = df.drop(["Loaned From","Contract Valid Until","GKReflexes","GKPositioning","GKKicking","GKHandling","GKDiving"],axis=1)
df = df.drop(["SlidingTackle","StandingTackle","Preferred Foot","Weight","Height","International Reputation","Release Clause"],axis=1)
df["Value"] = df["Value"].map(transform)
df["Wage"] = df["Wage"].map(transform)
df.head()

df.describe()

sn.set(rc = {'figure.figsize':(36,25)})
sn.heatmap(df.corr(), annot=True, cmap= 'YlGnBu')

df.fillna(0, inplace=True)
df.isnull().sum()

df_x = df.drop(["Overall"],axis=1).values
df_y = df["Overall"].values
print(len(df_x))

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, train_size = 0.60, random_state = 0)

randomF = RandomForestClassifier(criterion="entropy")

train=randomF.fit(x_train, y = y_train)
train_score = (randomF.score(x_train, y_train))
test_score = (randomF.score(x_test, y_test))
print(train_score,test_score)

predictions = randomF.predict(x_train[:150])
plt.plot(predictions[:150],color="red")
plt.plot(y_train[:150],color="green")
plt.show()

predictions = randomF.predict(x_test[:150])
plt.plot(predictions[:150],color="red")
plt.plot(y_test[:150],color="green")
plt.show()

regressor = (MLPRegressor(random_state = 0, activation = "relu", solver = "adam", 
                      hidden_layer_sizes = (35), alpha = 0.1, learning_rate = "adaptive", 
                      learning_rate_init = 0.1, max_iter = 1000))
train=regressor.fit(x_train, y = y_train)
train_score = (regressor.score(x_train, y_train))
test_score = (regressor.score(x_test, y_test))
print(train_score,test_score)

predictions = regressor.predict(x_train[:150])
plt.plot(predictions[:150],color="red")
plt.plot(y_train[:150],color="green")
plt.show()

predictions = regressor.predict(x_test[:150])
plt.plot(predictions[:150],color="red")
plt.plot(y_test[:150],color="green")
plt.show()