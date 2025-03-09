pip install matplotlib

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn import mean_squared_error as mse
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder

st.title('Stock_Prediction_Price')

st.info('Some Details of the price')


with st.expander('Data'):
  st.write('***Raw Date***')
  df = pd.read_csv("https://raw.githubusercontent.com/nivesh36923/nd-ml/master/stock_data.csv")
  df
df=df.rename(columns={'Unnamed: 0':'Date'})
df['Date'] = pd.to_datetime(df['Date'])
with st.expander('X'):
  X=df['Date']
  X
with st.expander('Y'):
  Y=df.drop('Date',axis=1)
  Y

'''plot of the following data'''
plt.figure(figsize=(12, 6))


plt.plot(df['Date'], df['Stock_1'], label='Stock_1 ($)', color='red')
plt.plot(df['Date'], df['Stock_2'], label='Stock_2 ($)', color='blue')
plt.plot(df['Date'], df['Stock_3'], label='Stock_3 ($)', color='green')
plt.plot(df['Date'], df['Stock_4'], label='Stock_4 ($)', color='yellow')
plt.plot(df['Date'], df['Stock_5'], label='Stock_5 ($)', color='black')


plt.title('Stock Prices between 2020-01-01 and 2020-12-30')
plt.xlabel('Date')
plt.ylabel('Close ($)')


plt.legend()

# Show the plot
plt.show()
  
