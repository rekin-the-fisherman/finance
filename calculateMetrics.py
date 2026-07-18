import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def calculate_metrics(ticker):

    dbConnectionString = os.getenv("DB_CONNECTION_STRING")
    engine = create_engine(dbConnectionString)

    existingData = pd.read_sql(f"SELECT * FROM stock_prices WHERE ticker = '{ticker}' ORDER BY date ASC", engine)

    if existingData.empty:
        return {"error": f"No data found for ticker {ticker}"}

    existingData['previous_close'] = existingData['close'].shift(1)
    existingData["daily_return"] = (existingData["close"] - existingData["previous_close"]) / existingData["previous_close"] * 100 
    volatility = existingData['daily_return'].std()
    annualized_volatility = volatility * np.sqrt(252)
    mean = existingData['daily_return'].mean()
    annualized_mean = mean * 252
    var = existingData["daily_return"].quantile(0.05)
    sharpe_ratio = (annualized_mean - 4) / annualized_volatility

    return {"sharpe_ratio" : sharpe_ratio, "var": var, "annualized_mean": annualized_mean, "annualized_volatility": annualized_volatility}
