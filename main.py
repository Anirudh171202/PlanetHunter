import os
import warnings
import math
from reduce_memory import reducememory
from plot_graphs import flux_dist
from plot_graphs import exoplanets, non_exoplanets
from data_anal import data_normalize
from reducing_features import reduce_features
import numpy as np 
import sklearn as sk
import pandas as pnds 
from sklearn.metrics import mean_squared_error, mean_absolute_error
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split 
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_score, recall_score,roc_curve,auc, f1_score, roc_auc_score,confusion_matrix, accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler, normalize
from scipy import ndimage
import seaborn as sns


warnings.filterwarnings('ignore')

std_scaler = StandardScaler()

train_data = pnds.read_csv('exoTrain.csv').fillna(0)
test_data = pnds.read_csv('exoTest.csv').fillna(0)

#flux_dist(train_data)

x_train = train_data.drop(["LABEL"], axis = 1)
y_train = train_data["LABEL"]

x_test = test_data.drop(["LABEL"], axis = 1)
y_test = test_data["LABEL"]

#exoplanets(x_train)
#exoplanets(x_test)

#non_exoplanets(x_train)
#print("Without normal\n", x_train.head())
#print("With normal")
#print("our version : ", sample_x_train.head())
x
