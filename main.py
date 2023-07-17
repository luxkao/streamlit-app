import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Title
st.title('Stock Price App')

# Sidebar
st.sidebar.title('Selecione a ação')
ticker = st.sidebar.text_input('Ticker', 'AAPL', max_chars = 10)

# Data
data = yf.download(ticker, start='2020-01-01', end='2023-07-15')

# Show data
st.subheader('Histórico de preços')
st.dataframe(data)

# Plot
fig = go.Figure()
fig.add_trace(go.Scatter(x = data.index, y = data['Close'], name = 'Fechamento'))
fig.update_layout(title = f"{ticker}", xaxis_title = 'Data', yaxis_title = 'Preço')
st.plotly_chart(fig, use_container_width = True)

# Plot candlestick
fig = go.Figure()
fig.add_trace(go.Candlestick(x = data.index, open = data['Open'], high = data['High'], low = data['Low'], close = data['Close'], name = 'Preço'))
fig.update_layout(title = f"{ticker}", xaxis_title = 'Data', yaxis_title = 'Preço')
st.plotly_chart(fig, use_container_width = True)

# Plot Moving Average
fig = go.Figure()
fig.add_trace(go.Scatter(x = data.index, y = data['Close'], name = 'Fechamento'))
fig.add_trace(go.Scatter(x = data.index, y = data['Close'].rolling(20).mean(), name = 'Média Móvel 20 dias'))
fig.update_layout(title = f"{ticker}", xaxis_title = 'Data', yaxis_title = 'Preço')
st.plotly_chart(fig, use_container_width = True)

