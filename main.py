from fastapi import FastAPI, Query
from tradingview_ta import TA_Handler, Interval
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Optional: Allow CORS if calling from Android app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/signal")
def get_signal(symbol: str = Query(..., description="Currency pair, e.g. EURUSD")):
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
        return {"error": str(e), "symbol": symbol}
