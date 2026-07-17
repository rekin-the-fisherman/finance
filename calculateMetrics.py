import pandas as pd
import numpy as np
from sqlalchemy import create_engine

dbConnectionString = "mysql+pymysql://root:@localhost:3306/project_finance"
engine = create_engine(dbConnectionString)

existingData = pd.read_sql("SELECT * FROM stock_prices WHERE ticker = 'AAPL' ORDER BY date ASC", engine)

existingData['previous_close'] = existingData['close'].shift(1)
existingData["daily_return"] = (existingData["close"] - existingData["previous_close"]) / existingData["previous_close"] * 100 
volatility = existingData['daily_return'].std()
annualized_volatility = volatility * np.sqrt(252)

print(annualized_volatility)
print(existingData)
