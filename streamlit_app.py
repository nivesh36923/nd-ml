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
