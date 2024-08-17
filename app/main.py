import streamlit as st
from app.data_fetcher import get_all_announcements
from app.utils import filter_trading_halt

TICKERS = ['AEE', 'REZ', '1AE', '1MC', 'NRZ']

def main():
    st.title("ASX Announcements Viewer")

    announcements = get_all_announcements(TICKERS)
    trading_halt_tickers = filter_trading_halt(announcements)

    selected_ticker = st.selectbox("Select a Ticker", TICKERS)

    st.subheader(f"Announcements for {selected_ticker}")
    for announcement in announcements.get(selected_ticker, []):
        st.text(announcement['headline'])

    st.subheader("Tickers with Trading Halt")
    for ticker in trading_halt_tickers:
        st.text(ticker)

if __name__ == "__main__":
    main()