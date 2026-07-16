import yfinance as yf
from sqlalchemy import create_engine

dbConnectionString = "mysql+pymysql://root:@localhost:3306/project_finance"


engine = create_engine(dbConnectionString)


data = yf.download('AAPL')

data.columns = data.columns.droplevel(1)

data = data.reset_index()

data['ticker'] = "AAPL"

data.to_sql('stock_prices', engine, if_exists='append', index=False)
            
