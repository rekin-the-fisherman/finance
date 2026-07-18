import yfinance as yf
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()



dbConnectionString = os.getenv("DB_CONNECTION_STRING")
engine = create_engine(dbConnectionString)


existingDates = pd.read_sql("SELECT date FROM stock_prices WHERE ticker = 'AAPL'", engine)


data = yf.download('AAPL', period="1y")

data.columns = data.columns.droplevel(1)

data = data.reset_index()

data['ticker'] = "AAPL"

existingDates['date'] = pd.to_datetime(existingDates['date'])

data = data[~data['Date'].isin(existingDates['date'])]

print(f"Inserting {len(data)} new rows")

data.to_sql('stock_prices', engine, if_exists='append', index=False)
print(existingDates)

            
