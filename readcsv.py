import pandas as pd 
import matplotlib
from datetime import datetime


#data_set = pd.read_csv('D:\\code\\pythonScripts\\padasexercise\\20200721.csv',encoding = "iso-8859-1")

data_set = pd.read_csv('D:\\temp\\200731.csv',encoding="utf-8")

#data_set = pd.read_table('D:\\code\\pythonScripts\\padasexercise\\20200721.txt')


#print(data_set.head(10))

for singlerow in data_set.iterrows():
    print(singlerow[1])
    print(singlerow[1][9])
    date_time_obj = datetime.strptime('20200730 ' + singlerow[1][9], '%Y%m%d %H:%M:%S')
    print(date_time_obj)
    print('------------')