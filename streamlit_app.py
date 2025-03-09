import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.metrics import mean_squared_error 
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

df['f1'] = df['Stock_1'].shift(1)
df['f2'] = df['Stock_1'].shift(2)
df['f3'] = df['Stock_1'].shift(3)
df['f4'] = df['Stock_1'].shift(4)
df['f5'] = df['Stock_1'].shift(5)
df['f6'] = df['Stock_1'].shift(6)
df['f7'] = df['Stock_1'].shift(7)

with st.expander('Data'):
  df
df.dropna(inplace=True)
with st.expander('Data'):
  df


train_size = int(len(df)*0.8)
train,test= df.iloc[:train_size],df.iloc[train_size:]

X_train, y_train = train.drop(['Date','Stock_1','Stock_2','Stock_3','Stock_4','Stock_5'], axis=1), train['Stock_1']
X_test, y_test = test.drop(['Date','Stock_1','Stock_2','Stock_3','Stock_4','Stock_5'], axis=1), test['Stock_1']



model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=3)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
st.info(f"Mean Squared Error: {mse:.4f}")



X_combined = pd.concat([X_train, X_test], ignore_index=True)
with st.expander('X_combined'):
  X_combined
predictions = model.predict(X_combined)
pred_df = pd.DataFrame(predictions)
y_combined = pd.concat([y_train, y_test], ignore_index=True)
with st.expander('y_combined'):
  y_combined
with st.expander('y_train'):
  y_train
with st.expander('pred_df'):
  pred_df


# Plot each stock separately with correct labels and colors
fig2, ax2 = plt.subplots(figsize=(12, 6))
ax2.plot(df['Date'], pred_df, label='predicted ($)', color='red')

ax2.plot(df['Date'], y_combined, label='actual ($)', color='blue')
ax2.plot(df['Date'], df['Stock_1'], label='df($)', color='green')
# Titles and labels
ax2.set_title('Stock Prices between 2020-01-01 and 2020-01-30')
ax2.set_xlabel('Date')
ax2.set_ylabel('Close ($)')


# Add legend
ax2.legend()

# Show the plot
st.pyplot(fig2)
