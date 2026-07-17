import pandas as pd
import numpy as np
from sqlalchemy import create_engine

dbConnectionString = "mysql+pymysql://root:@localhost:3306/project_finance"
engine = create_engine(dbConnectionString)

existingData = pd.read_sql("SELECT * FROM stock_prices WHERE ticker = 'AAPL' ORDER BY date ASC", engine)

existingData['previous_close'] = existingData['close'].shift(1)
existingData["daily_return"] = (existingData["close"] - existingData["previous_close"]) / existingData["previous_close"] * 100 
volatility = existingData['daily_return'].std()
mean = existingData['daily_return'].mean()
annualized_mean = mean * 252
annualized_volatility = volatility * np.sqrt(252)
sharpe_ratio = (annualized_mean - 4) / annualized_volatility

print(annualized_mean)
print(annualized_volatility)
print(sharpe_ratio)
