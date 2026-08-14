import yfinance as yf
import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

tickers = ["NVDA", "AMD", "INTC", "AVGO", "QCOM", "TSM", "MRVL", "MU", "TXN", "AMAT", "ASML", "LRCX", "KLAC", "STX", "WDC", "TER", "MSFT", "CRM", "ADBE", "ORCL", "INTU", "NOW", "PANW", "CRWD", "FTNT", "ZS", "NET", "SNOW", "DDOG", "PLTR", "IBM", "SAP", "SHOP", "GOOGL", "META", "AMZN", "AAPL", "NFLX", "TSLA", "UBER", "ABNB", "COIN", "PYPL", "OKTA", "SENT", "INOD", "TEM", "BTBT", "DOX", "CRDO", "LEU", "FICO", "ACN"]
for t in tickers:
    try:
        info = yf.Ticker(t).info
        sector = info.get("sector")
        print(f"{t}: {sector}")
    except Exception as e:
        print(f"{t}: Error")
