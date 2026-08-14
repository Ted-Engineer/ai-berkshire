import yfinance as yf
import json

tickers = ["VRT", "MRVL", "MU", "ADBE", "LRCX", "CRWD", "INTU", "CRM"]
results = {}

for t in tickers:
    try:
        stock = yf.Ticker(t)
        info = stock.info
        results[t] = {
            "price": info.get("currentPrice") or info.get("regularMarketPrice"),
            "marketCap": info.get("marketCap"),
            "pe_ttm": info.get("trailingPE"),
            "pe_fwd": info.get("forwardPE"),
            "ps": info.get("priceToSalesTrailing12Months"),
            "pb": info.get("priceToBook"),
            "revenue": info.get("totalRevenue"),
            "revenueGrowth": info.get("revenueGrowth"),
            "grossMargin": info.get("grossMargins"),
            "operatingMargin": info.get("operatingMargins"),
            "netMargin": info.get("profitMargins"),
            "roe": info.get("returnOnEquity"),
            "fcf": info.get("freeCashflow"),
            "debtToEquity": info.get("debtToEquity"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "shortName": info.get("shortName"),
            "beta": info.get("beta"),
            "52wHigh": info.get("fiftyTwoWeekHigh"),
            "52wLow": info.get("fiftyTwoWeekLow"),
        }
        print(f"{t}: OK - price={results[t]['price']}")
    except Exception as e:
        results[t] = {"error": str(e)}
        print(f"{t}: ERROR - {e}")

print("---JSON_START---")
print(json.dumps(results, indent=2, default=str))
print("---JSON_END---")
