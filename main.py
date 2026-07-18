from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import calculateMetrics as cm

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/metrics/{ticker}")
def get_metrics(ticker: str):
    return cm.calculate_metrics(ticker)