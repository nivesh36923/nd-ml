import streamlit as st
import pandas as pd

st.title('Stock_Prediction_Price')

st.info('Some Details of the price')


with st.expander('Data'):
  st.write('***Raw Date***')
  df = pd.read_csv("https://raw.githubusercontent.com/nivesh36923/nd-ml/master/stock_data.csv")
  df

with st.expander('X'):
  X=df['Date']
  X
with st.expander('Y'):
  Y=df.drop('Date',axis=1)
  Y

  
