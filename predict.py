# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:28:26 2017

@author: caibo
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
import os

def get_data(file_name):
    data=pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    for single_square_feet,single_price_value in zip(
            data['square_feet'],data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append([float(single_price_value)])
    return X_parameter,Y_parameter

x,y=get_data(r'C:\Users\caibo\Desktop\allfiles\predict_hourse.csv') 
     
def linear_model_main(X_parameters,Y_parameters,predict_value):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions
predictvalue=700
result=linear_model_main(x,y,predictvalue)

def show_linear_line(X_parameters,Y_parameters):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color='blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()
show_linear_line(x,y)











