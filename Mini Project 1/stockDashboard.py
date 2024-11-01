import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import time
import pandas as pd

st.set_page_config(page_title="Stock Market Dashboard", page_icon=":bar_chart:", layout="wide")
# Function to get period and interval based on timeframe
def get_period(timeframe):
    if timeframe == "1D":
        return "1d", "1m"  # 1-day period with 1-minute intervals
    elif timeframe == "1M":
        return "1mo", "1d"  # 1-month period with daily data
    elif timeframe == "6M":
        return "6mo", "1d"  # 6-month period with daily data
    elif timeframe == "1Y":
        return "1y", "1d"  # 1-year period with daily data
    else:
        return "max", "1d"  # Full available history with daily data

# Streamlit App Title
st.title("Stock Market Dashboard")

# Sidebar Layout
st.sidebar.title("Fill the Details")
tickers = st.sidebar.text_input("Enter Ticker Symbols (comma-separated)", placeholder="E.g. AAPL, GOOGL")
chart_type = st.sidebar.selectbox("Select Chart Type", ["Candlestick", "Line Chart"])
indicators = st.sidebar.multiselect('Technical Indicators', ['SMA_50', 'SMA_200'])
time_period = st.sidebar.selectbox("Time Period", ["1D", "1M", "6M", "1Y", "All"])

# Process tickers
ticker_list = [ticker.strip().upper() for ticker in tickers.split(",") if ticker]

if st.sidebar.button("Update"):
    if len(ticker_list) == 1: 
        # Single stock view
        tickerSymbol = ticker_list[0]
        yfTicker = yf.Ticker(tickerSymbol)
        stock_info = yfTicker.info
        period, interval = get_period(time_period)
        history_data = yfTicker.history(period=period, interval=interval)
        current_price = stock_info.get('currentPrice', 0)
        price_change = stock_info.get('regularMarketChange', 0)
        percent_change = stock_info.get('regularMarketChangePercent', 0)
        todays_high = stock_info.get('dayHigh', 0)
        todays_low = stock_info.get('dayLow', 0)
        volume = stock_info.get('volume', 0)
        traded_value = volume * current_price / 1e9
        marketCap = stock_info.get('marketCap', 0) / 1e9

        # Display stock metrics
        with st.container():
            with st.spinner("Loading..."):
                time.sleep(4)
            st.metric(label=f"**{stock_info['longName']} • {tickerSymbol}**", value=f"{current_price:.2f} USD", delta=f"{price_change:.2f} ({percent_change:.2f}%)")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("🔼 High", f"{todays_high:.2f} USD")
        col2.metric("🔻 Low", f"{todays_low:.2f} USD")
        col3.metric("📊 Volume", f"{volume:,}")

        chart_tab, history_tab, price_summary = st.tabs(["Chart", "History", "Price Summary"])

        # Plot chart
        fig = go.Figure()
        with chart_tab:
            if chart_type == 'Candlestick':
                fig.add_trace(go.Candlestick(x=history_data.index, open=history_data['Open'], high=history_data['High'], low=history_data['Low'], close=history_data['Close'], name='Candlestick'))
            elif chart_type == 'Line Chart':
                fig.add_trace(go.Scatter(x=history_data.index, y=history_data['Close'], name='Line Chart', mode='lines'))

            # Add indicators
            for indicator in indicators:
                if indicator == 'SMA_50' and len(history_data) >= 50:
                    history_data['SMA_50'] = history_data['Close'].rolling(window=50).mean()
                    fig.add_trace(go.Scatter(x=history_data.index, y=history_data['SMA_50'], name='SMA 50', mode='lines', line=dict(color='blue', width=1.5)))
                if indicator == 'SMA_200' and len(history_data) >= 200:
                    history_data['SMA_200'] = history_data['Close'].rolling(window=200).mean()
                    fig.add_trace(go.Scatter(x=history_data.index, y=history_data['SMA_200'], name='SMA 200', mode='lines', line=dict(color='red', width=1.5)))

            fig.update_layout(title=f'{tickerSymbol} {time_period.upper()} Chart', xaxis_title='Date', yaxis_title='Price (USD)', xaxis_rangeslider_visible=False)
            st.plotly_chart(fig, use_container_width=True)

        with history_tab:
            st.dataframe(history_data, use_container_width=True)

        with price_summary:
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"📈 **52 Week High:** {stock_info.get('fiftyTwoWeekHigh', 'N/A')} USD")
                st.write(f"💰 **Market Cap:** {marketCap:.2f} B USD")
                st.write(f"💹 **PE Ratio:** {round(stock_info.get('trailingPE', 'N/A'),2) }")
            with col2:
                st.write(f"📉 **52 Week Low:** {stock_info.get('fiftyTwoWeekLow', 'N/A')} USD")
                st.write(f"💵 **Dividend Yield:** {round(stock_info.get('dividendYield', 'N/A') * 100,2)} %")
                st.write(f"⚖️ **Beta:** {stock_info.get('beta', 'N/A')}")
                st.write(f"📈 **Traded Value:** {traded_value:.2f} B USD")

    elif len(ticker_list) == 2:
        # Combined chart view for two stocks
        fig = go.Figure()

        combined_data = {}

        # Loop through both tickers
        for tickerSymbol in ticker_list:
            yfTicker = yf.Ticker(tickerSymbol)
            period, interval = get_period(time_period)
            history_data = yfTicker.history(period=period, interval=interval)

            if not history_data.empty and len(history_data) >= 2:
                combined_data[tickerSymbol] = history_data[['Open', 'High', 'Low', 'Close', "Volume"]]
                if chart_type == 'Candlestick':
                    fig.add_trace(go.Candlestick(x=history_data.index, open=history_data['Open'], high=history_data['High'], low=history_data['Low'], close=history_data['Close'], name=f'{tickerSymbol} Candlestick'))
                elif chart_type == 'Line Chart':
                    fig.add_trace(go.Scatter(x=history_data.index, y=history_data['Close'], name=f'{tickerSymbol} Line', mode='lines'))

                # Add indicators
                for indicator in indicators:
                    if indicator == 'SMA_50' and len(history_data) >= 50:
                        history_data['50-day MA'] = history_data['Close'].rolling(window=50).mean()
                        fig.add_trace(go.Scatter(x=history_data.index, y=history_data['50-day MA'], name=f'{tickerSymbol} SMA 50', mode='lines', line=dict(width=1.5)))
                    if indicator == 'SMA_200' and len(history_data) >= 200:
                        history_data['200-day MA'] = history_data['Close'].rolling(window=200).mean()
                        fig.add_trace(go.Scatter(x=history_data.index, y=history_data['200-day MA'], name=f'{tickerSymbol} SMA 200', mode='lines', line=dict(width=1.5)))\

        fig.update_layout(title=f'Combined Chart for {ticker_list[0]} and {ticker_list[1]} - {time_period} Period', xaxis_title='Date', yaxis_title='Price (USD)', xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("Performance Insights"):
            # Define the main columns to separate each stock's data
            col1, col2 = st.columns([1,1])
            
            # Performance Insights for the first stock (ticker_list[0])
            with col1:
                st.write(f"{ticker_list[0]} Performance Summary")
                stock_info = yf.Ticker(ticker_list[0]).info
                col1_left, col1_right = st.columns(2)
                with col1_left:
                    st.write(f"📈 **52 Week High:** {stock_info.get('fiftyTwoWeekHigh', 'N/A')} USD")
                    st.write(f"💰 **Market Cap:** {stock_info.get('marketCap', 'N/A') / 1e9:.2f} B USD")
                    st.write(f"💹 **PE Ratio:** {round(stock_info.get('trailingPE', 'N/A'),2)}")
                with col1_right:
                    st.write(f"📉 **52 Week Low:** {stock_info.get('fiftyTwoWeekLow', 'N/A')} USD")
                    st.write(f"💵 **Dividend Yield:** {round(stock_info.get('dividendYield', 'N/A') * 100,2)} %")
                    st.write(f"⚖️ **Beta:** {stock_info.get('beta', 'N/A')}")
                    st.write(f"📊 **Volume:** {stock_info.get('volume', 'N/A') / 1e7:.2f} M USD")

            with col2:
                st.write(f"{ticker_list[1]} Performance Summary")
                stock_info_2 = yf.Ticker(ticker_list[1]).info
                col2_left, col2_right = st.columns(2)
                with col2_left:
                    st.write(f"📈 **52 Week High:** {stock_info_2.get('fiftyTwoWeekHigh', 'N/A')} USD")
                    st.write(f"💰 **Market Cap:** {stock_info_2.get('marketCap', 'N/A') / 1e9:.2f} B USD")
                    st.write(f"💹 **PE Ratio:** {round(stock_info.get('trailingPE', 'N/A'),2)}")
                with col2_right:
                    st.write(f"📉 **52 Week Low:** {stock_info_2.get('fiftyTwoWeekLow', 'N/A')} USD")
                    st.write(f"💵 **Dividend Yield:** {round(stock_info_2.get('dividendYield', 'N/A') * 100,2)} %")
                    st.write(f"⚖️ **Beta:** {stock_info_2.get('beta', 'N/A')}")
                    st.write(f"📊 **Volume:** {stock_info_2.get('volume', 'N/A') / 1e7:.2f} M USD")

        with st.expander("Historical Data",):
            combined_history = pd.concat(combined_data.values(), axis=1,keys=combined_data.keys())
            combined_history.columns = [f'{ticker}_{col}' for ticker,col in combined_history.columns]
            st.dataframe(combined_history, use_container_width=True)
    
    else:
        st.warning("You can compare atmost 2 stocks at a time.")
