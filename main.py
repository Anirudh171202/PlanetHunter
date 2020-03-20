import os
import warnings
import math
from reduce_memory import reducememory
from plot_graphs import flux_dist
from plot_graphs import exoplanets, non_exoplanets

import numpy as np 
import sklearn as sk
import pandas as pnds 



warnings.filterwarnings('ignore')



train_data = pnds.read_csv('exoTrain.csv').fillna(0)
test_data = pnds.read_csv('exoTest.csv').fillna(0)

#flux_dist(train_data)

x_train = train_data.drop(["LABEL"], axis = 1)
y_train = train_data["LABEL"]

x_test = test_data.drop(["LABEL"], axis = 1)
y_test = test_data["LABEL"]

exoplanets(x_train)
#exoplanets(x_test)

non_exoplanets(x_train)




