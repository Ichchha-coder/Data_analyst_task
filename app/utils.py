def filter_trading_halt(announcements):
    trading_halt_tickers = []
    for ticker, items in announcements.items():
        for announcement in items:
            if "Trading Halt" in announcement['headline']:
                trading_halt_tickers.append(ticker)
                break
    return trading_halt_tickers