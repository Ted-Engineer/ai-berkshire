import yfinance as yf
import pandas as pd
import ssl
import datetime

ssl._create_default_https_context = ssl._create_unverified_context

tickers = [
    'AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AMZN', 'META', 'TSLA', 'AVGO', 'QCOM', 'AMD', 
    'ASML', 'LRCX', 'KLAC', 'AMAT', 'MU', 'TSM', 'MRVL', 'ADBE', 'CRM', 'ORCL', 
    'INTU', 'NOW', 'PANW', 'CRWD', 'FTNT', 'ZS', 'NET', 'SNOW', 'DDOG', 'PLTR', 
    'IBM', 'SAP', 'SHOP', 'NFLX', 'UBER', 'ABNB', 'COIN', 'PYPL', 'OKTA', 'SMCI', 
    'DELL', 'HPE', 'ANET', 'CSCO', 'VRT', 'ETN', 'PWR', 'CEG', 'VST', 'ISRG', 
    'RBLX', 'U'
]

data = []
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=90)

print(f"Starting scan for {len(tickers)} tickers...")

for t in tickers:
    try:
        info = yf.Ticker(t).info
        hist = yf.Ticker(t).history(start=start_date, end=end_date)
        if not hist.empty:
            chg = (hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0] * 100
            data.append({
                'ticker': t,
                'sector': info.get('sector', 'Unknown'),
                'industry': info.get('industry', 'Unknown'),
                'marketCap': info.get('marketCap', 0),
                'chg_3m': chg
            })
    except Exception as e:
        print(f"Error fetching {t}: {e}")

df = pd.DataFrame(data)
summary = df.groupby(['sector', 'industry']).agg({
    'marketCap': 'sum',
    'chg_3m': 'mean'
}).reset_index()

summary = summary.sort_values(by='marketCap', ascending=False)
print("\n--- Industry Funnel Layer 1 Results ---")
print(summary.to_string(index=False))
