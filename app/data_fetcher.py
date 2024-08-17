import requests

def fetch_announcements(TICKER):
    url = f"https://www.asx.com.au/asx/1/company/{TICKER}/announcements?count=20&market_sensitive=false"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_all_announcements(TICKERS):
    all_announcements = {}
    for TICKER in TICKERS:
        try:
            announcements = fetch_announcements(TICKER)
            all_announcements[TICKER] = announcements
        except Exception as e:
            print(f"Error fetching data for {TICKER}: {e}")
    return all_announcements