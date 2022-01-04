import requests as r
import json
import pandas as pd
from datetime import datetime
import mplfinance as fplt


def getTodayInfo(ticker: str ):

	'''
	Will get a lot of data on the cryptocurrency including name, symbol, social media data

	params
	ticker, str: the name of the cryptocuyrrency
	'''
	url = f'https://api.coingecko.com/api/v3/coins/{ticker}/history?date={datetime.now().strftime("%d-%m-%Y")}'

	response = json.loads(r.get(url).text)

	return response

def getOHLC(ticker : str, days: int = 365):
	'''
	Get's OHLC graph for a ticker for specified amt of time.
	You can set the amount of days, but for the purposes of it's usage it's set to 365 days

	Params
	ticker, str : the name of the cryptocurrency
	days, int : days for the ohlc data, set to default at 365
	'''
	url = f'https://api.coingecko.com/api/v3/coins/{ticker}/ohlc?vs_currency=usd&days={365}'

	try:
		#please don't ask this was a nightmare to write lmao
		df = pd.DataFrame(
			[[datetime.fromtimestamp(int(str(x[0])[:-3])).strftime('%Y-%m-%d'), x[1], x[2], x[3], x[4]] for x in json.loads(r.get(url).text)][::-1],
			#this is to solve a minor issue in graphs I ntoiced ^^^^^^^^^^
			columns = ["Date", "Open", "High", "Low", "Close"]
			)[::-1]
		df.index = pd.DatetimeIndex(df['Date'])
		fplt.plot(df,
			type="candle",
			title=f'{ticker} for {days} days',
	        ylabel='Price ($)',
	        savefig=f'static/temp/{ticker}_for_{days}_days.png')

		return f'static/temp/{ticker}_for_{days}_days.png'
	except:
		return ""
