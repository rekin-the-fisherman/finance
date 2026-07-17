from fastapi import FastAPI

import calculateMetrics as cm

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/metrics/{ticker}")
def get_metrics(ticker: str):
    return cm.calculate_metrics(ticker)