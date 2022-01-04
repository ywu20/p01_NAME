import requests as r
import json


def grabByTicker(symbol : str):
	'''
	Supports crypto and stocks

	This returns a list of these (not more than 10).

	{'title': 'Vaxart Rises 3% After Signing License Agreement With Altesa Biosciences',
	'description': '(RTTNews) - Shares of Vaxart, Inc. (VXRT) are climbing more than 3% Wednesday morning after the clinical-stage biotechnology company signed a lice...',
	'content': "(RTTNews) - Shares of Vaxart, Inc. (VXRT) are climbing more than 3% Wednesday morning after the clinical-stage biotechnology company signed a license agreement with Altesa Biosciences, Inc. for Vaxart's investigational antiviral drug Vapendavir.\nAs p... [518 chars]",
	'url': 'https://markets.businessinsider.com/news/stocks/vaxart-rises-3-after-signing-license-agreement-with-altesa-biosciences-1030586379',
	'image': 'https://markets.businessinsider.com/apple-touch-icon.png',
	'publishedAt': '2021-07-07T14:16:18Z',
	'source': {'name': 'Business Insider', 'url': 'https://markets.businessinsider.com'}}
	'''

	url = "https://gnews.io/api/v4/search?"

	with open("keys/key_news.txt", "r") as f:
		key = str(f.readline())

	
	args = {
		"q": symbol,
		"token" : key,
		"lang": "en"}

	return json.loads(r.get(url, params=args).text)["articles"]
