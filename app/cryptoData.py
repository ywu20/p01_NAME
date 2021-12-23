import requests as r
import json
import pandas as pd
from datetime import datetime
import mplfinance as fplt

def getOHLC(ticker : str, days: int = 365):
	url = f'https://api.coingecko.com/api/v3/coins/{ticker}/ohlc?vs_currency=usd&days={365}'
	df = pd.DataFrame(
		[[datetime.fromtimestamp(int(str(x[0])[:-3])).strftime('%Y-%m-%d'), x[1], x[2], x[3], x[4]] for x in json.loads(r.get(url).text)],
		columns = ["Date", "Open", "High", "Low", "Close"]
		)[::-1]
	df.index = pd.DatetimeIndex(df['Date'])
	fplt.plot(df, 
		type="candle", 
		title=f'{ticker} for {days} days',
        ylabel='Price ($)',
        savefig=f'static/temp/{ticker}_for_{days}_days.png')
#getOHLC("bitcoin")