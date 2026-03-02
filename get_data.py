from datetime import datetime, timedelta
import yfinance as yf
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(PROJECT_DIR, 'data')

# makedir for data
os.makedirs(DATA_DIR, exist_ok=True)

# Tickers organized by asset class (subdirectory name -> ticker list)
ticker_groups = {
    'fx': ['EURUSD=X', 'GBPUSD=X', 'USDJPY=X', 'USDCHF=X', 'AUDUSD=X', 'NZDUSD=X', 'USDCAD=X'],
    'commodities': ['GC=F', 'CL=F', 'HG=F'],  # Gold, Crude Oil, Copper
    'equities': ['^GSPC', '^VIX', '^N225', '^GDAXI', '^FTSE'],  # S&P500, VIX, Nikkei, DAX, FTSE
    'bonds': ['^TNX', '^IRX'],  # 10Y, 2Y yields
    'currency_etfs': ['FXE', 'FXY', 'FXB', 'FXA', 'FXC'],
    'risk': ['HYG', 'EEM'],  # High-yield bonds, EM equities
    'crypto': ['BTC-USD'],
}


for subdir, tickers in ticker_groups.items():
    subdir_path = os.path.join(DATA_DIR, subdir)
    os.makedirs(subdir_path, exist_ok=True)
    
    for ticker in tickers:
        df = yf.download(ticker, period='7d', interval='1m')
        print(len(df))
        # get first and last timestamps
        first_timestamp = df.index[0]
        last_timestamp = df.index[-1]

        # save dataframe to csv
        csv_filename = os.path.join(subdir_path, f'{ticker}_1m_{first_timestamp.date()}_to_{last_timestamp.date()}.csv')
        df.to_csv(csv_filename)
        print(f'Data saved to {csv_filename}')
