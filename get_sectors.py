import yfinance as yf
import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "BRK-B", "UNH", "JPM", "XOM", "AVGO", "LLY", "V", "MA", "ASML", "COST", "PG", "HD", "JNJ", "ABBV", "ADBE", "CRM", "AMD", "CVX", "PEP", "KO", "NFLX", "ORCL", "TMO", "AVW"]
data = []
for t in tickers:
    try:
        info = yf.Ticker(t).info
        data.append({"ticker": t, "sector": info.get("sector"), "industry": info.get("industry")})
    except Exception as e:
        print(f"Error fetching {t}: {e}")

df = pd.DataFrame(data)
print(df)

