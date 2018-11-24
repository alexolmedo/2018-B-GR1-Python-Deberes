# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 07:54:06 2018

@author: Alexander
"""

import pandas as pd
import os

CSV_PATH = "C://Users//Alexander//Documents//Python//deberes//titanic.csv"


#data_frame_artwork = pd.read_csv(
#        CSV_PATH,
#        index_col= 'PassengerId',
#        usecols = ['PassengerId','Survived'])

columnas_a_utilizar = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']

data_frame_pasajeros = pd.read_csv(
        CSV_PATH,
        index_col= 'PassengerId',
        usecols = columnas_a_utilizar)

data_frame_pasajeros['Survived'].value_counts()

data_frame_pasajeros.groupby(['Pclass'])['Survived'].value_counts()

data_frame_pasajeros.groupby(['Sex'])['Survived'].value_counts()








