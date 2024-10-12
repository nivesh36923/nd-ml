import streamlit as st
import pandas as pd

st.title('👽MACHINE LEARNING')

st.info('hey! This is L')


with st.expander('Data'):
  st.write('***Raw Date***')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
