from fastapi import FastAPI
from tradingview_ta import TA_Handler, Interval, Exchange
import concurrent.futures
import os
import uvicorn

app = FastAPI()

symbols = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF"]

def fetch_signal(symbol):
    try:
        handler = TA_Handler(
            symbol=symbol,
            screener="forex",
            exchange="FX_IDC",
            interval=Interval.INTERVAL_5_MINUTES
        )
        analysis = handler.get_analysis()
        return {
            "symbol": symbol,
            "summary": analysis.summary,
            "indicators": analysis.indicators
        }
    except Exception as e:
        return {"symbol": symbol, "error": str(e)}

@app.get("/signals")
def get_signals():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_signal, symbols))
    return results

# Start Uvicorn dynamically for Railway
if _name_ == "_main_":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
