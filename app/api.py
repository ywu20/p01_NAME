#Name — Andrew Juang, Eliza Knapp, Patrick Ging, Yuqing Wu
#Softdev
#P01: ArRESTed Development
#2021-12-10

import yfinance as yf

def update_data(stockName : str):
    '''
    pull_data

    args:
        str stockName, a ticker for the security

    returns a dictionary regarding info on a stock with ticker stockName

    returns an empty dictionary if the stock ticker doesn't exist

    There is a wait time on this function as it is using the wrapper API
    so we should keep that in mind....


    '''
    try:
        stockInfo = yf.Ticker(stockName.upper()).info
        stockDiv = yf.Ticker(stockName.upper()).news
    except:
        return {}

    if stockInfo.get("regularMarketPrice") is None:
        #the wrapper api will have @ none
        #if the ticker doesn't exist.
        #might update in the future?
        return {}
    else:
        #some properties of it, will update as needed
        return {
        "officialName" : stockInfo["longName"],
        "price" : stockInfo["currentPrice"],
        "website": stockInfo["website"],
        "sector" : stockInfo["sector"],
        "description": stockInfo["longBusinessSummary"],

        }
