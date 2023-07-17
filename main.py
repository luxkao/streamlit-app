import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Title
st.title('Stock Price App')

# Sidebar
st.sidebar.title('Selecione a ação')
ticker = st.sidebar.text_input('Ticker', 'AAPL', max_chars = 10)

# Data
data = yf.download(ticker, start='2020-01-01', end='2023-16-07')

# Show data
st.subheader('Histórico de preços')
st.dataframe(data)

# Plot
fig = go.Figure()
fig.add_trace(go.Scatter(x = data.index, y = data['Close'], name = 'Fechamento'))
fig.update_layout(title = f"{ticker}", xaxis_title = 'Data', yaxis_title = 'Preço')
st.plotly_chart(fig, use_container_width = True)