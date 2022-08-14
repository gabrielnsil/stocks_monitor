import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

# Monitor de Ações *WebApp*

Aqui são mostrados o **preço de fechamento** e **volume negociado** da Petrobras (PETR4.SA)
Os dados usados nessa aplicação são extraídos do Yahoo! Finance.
""")

# Define a ticker symbol to be used
tickerSymbol = "PETR4.SA"

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this tickerData
tickerDf = tickerData.history(period="1d", start="2010-01-01", end = "2022-08-01")

# Open High Low Close Volume Dividends Stock Splits

st.write("""

### Preço de Fechamento

""")

st.line_chart(tickerDf.Close)

st.write("""

### Volume Negociado Diário

""")
st.line_chart(tickerDf.Volume)
