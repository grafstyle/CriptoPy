from binance import Client
import pandas as pd 
import datetime as dt 
import mplfinance as mpl 
from decouple import config

api_key = config('API_Key')
api_secret = config('Secret_Key')
client = Client(api_key, api_secret)

#price = client.get_symbol_ticker(symbol="ETHUSDT")

price = client.get_symbol_ticker(symbol="BTCUSDT")
print(price)


asset="BTCUSDT"
start="2023.1.1"
end="2024.1.1"
timeframe="1d"
df= pd.DataFrame(client.get_historical_klines(asset, timeframe, start, end))
df=df.iloc[:,:6]
df.columns=["Date", "Open", "High", "Low", "Close", "Volume"]
df=df.set_index("Date")
df.index=pd.to_datetime(df.index,unit="ms")
df=df.astype("float")
print(df)
mpl.plot(df, type="candle", volume=True, mav=7)

