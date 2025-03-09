import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.metrics import mean_squared_error as mse
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder

st.title('Stock_Prediction_Price')

st.info('Some Details of the price')


with st.expander('Data'):
  st.write('***Raw Date***')
  df = pd.read_csv("https://raw.githubusercontent.com/nivesh36923/nd-ml/master/stock_data.csv")
  df=df.rename(columns={'Unnamed: 0':'Date'})
  df['Date'] = pd.to_datetime(df['Date'])
  df

with st.expander('X'):
  X=df['Date']
  X
with st.expander('Y'):
  Y=df.drop('Date',axis=1)
  Y

'''plot of the following data'''
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(df['Date'], df['Stock_1'], label='Stock_1 ($)', color='red')
ax.plot(df['Date'], df['Stock_2'], label='Stock_2 ($)', color='blue')
ax.plot(df['Date'], df['Stock_3'], label='Stock_3 ($)', color='green')
ax.plot(df['Date'], df['Stock_4'], label='Stock_4 ($)', color='yellow')
ax.plot(df['Date'], df['Stock_5'], label='Stock_5 ($)', color='black')

ax.set_title('Stock Prices between 2020-01-01 and 2020-12-30')
ax.set_xlabel('Date')
ax.set_ylabel('Close ($)')
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)
