import streamlit as st
import pandas as pd

st.title('👽MACHINE LEARNING')

st.info('hey! This is L')


with st.expander('Data'):
  st.write('***Raw Date***')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

with st.expander('X'):
  X=df.drop('species',axis=1)
  X
with st.expander('Y'):
  Y=df.species
  Y

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')
# data preparation 
with st.sidebar:
  st.header('input features')
  island=st.selectbox('island', ('Biscoe', 'Drean','Torgersen' ))
  gender=st.selectbox('gender', ('mate','female'))
  bill_length_m = st.slider('Bill length (mn)', 32.1, 59.6, 43.9)
  
