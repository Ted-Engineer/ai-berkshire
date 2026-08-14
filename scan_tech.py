import yfinance as yf
import pandas as pd
import ssl
import datetime
from multiprocessing import Pool

ssl._create_default_https_context = ssl._create_unverified_context

def fetch_info(t):
    try:
        info = yf.Ticker(t).info
        return {'ticker': t, 'sector': info.get('sector', 'Unknown'), 'industry': info.get('industry', 'Unknown')}
    except Exception as e:
        return {'ticker': t, 'sector': 'Error', 'industry': str(e)}

if __name__ == "__main__":
    tickers = [
        'AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AMZN', 'META', 'TSLA', 'AVGO', 'QCOM', 'AMD', 
        'ASML', 'LRCX', 'KLAC', 'AMAT', 'MU', 'TSM', 'MRVL', 'ADBE', 'CRM', 'ORCL', 
        'INTU', 'NOW', 'PANW', 'CRWD', 'FTNT', 'ZS', 'NET', 'SNOW', 'DDOG', 'PLTR', 
        'IBM', 'SAP', 'SHOP', 'NFLX', 'UBER', 'ABNB', 'COIN', 'PYPL', 'OKTA', 'SMCI', 
        'DELL', 'HPE', 'ANET', 'CSCO', 'VRT', 'ETN', 'PWR', 'CEG', 'VST', 'ISRG', 
        'RBLX', 'U'
    ]

    print(f"Starting scan for {len(tickers)} tickers...")
    with Pool(processes=10) as pool:
        results = pool.map(fetch_info, tickers)

    df = pd.DataFrame(results)
    summary = df.groupby(['sector', 'industry']).size().reset_index(name='count')
    print("\n--- Industry Funnel Layer 1 Results ---")
    print(summary.to_string(index=False))
