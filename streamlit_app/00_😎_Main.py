import streamlit as st

st.set_page_config(
    page_title="Stock Prediction App",
    page_icon="📈",
)

st.markdown(
    """# 📈 **Stock Price Prediction**
### **Machine learning project by 
Avishi Singh (102203055) and Shreya Singh (102203070)**

**It is an ML-powered stock price prediction app built with Python and Streamlit. It utilizes machine learning models to forecast stock prices and help investors make data-driven decisions.**

## 🏗️ **How It's Built**

It is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **YFinance** - To fetch financial data from Yahoo Finance API
- **StatsModels** - To build the ARIMA time series forecasting model
- **Seaborn** - To create interactive financial charts


## 🎯 **Key Features**

- **Real-time data** - Fetch latest prices and fundamentals 
- **Financial charts** - Interactive historical and forecast charts
- **ARIMA forecasting** - Make statistically robust predictions
- **Responsive design** - Works on all devices

## 🔄 **Process Overview**

- **User selects stock** - The user inputs the stock ticker for which predictions are needed.
- **Fetch historical stock data** - Historical stock data is fetched using Yahoo Finance (via `yfinance`).
- **Clean and preprocess data** - The data is cleaned, retaining only the 'Close' prices for prediction.
- **Train ARIMA model** - The ARIMA model is trained using the cleaned historical data.
- **Generate predictions for the next 90 days** - Forecasting for the next 90 days is done using the trained ARIMA model.
- **Visualize predictions and trends** - Predictions and historical trends are displayed interactively using Plotly and Streamlit.



## **⚖️ Disclaimer**
**This is not financial advice, it is only made for learning. No guarantee of trading performance.**
"""
)
