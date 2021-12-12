#Name — Andrew Juang, Eliza Knapp, Patrick Ging, Yuqing Wu
#Softdev
#P01: ArRESTed Development
#2021-12-10

import yfinance as yf


def update_data(stock):
    """
    Gets the newest data for a stock
        parameter (str): symbol / name (depending on which one the apis use
               to identify the stock )of the stock we want data for.
        returns (dictionary): {"name / symbol" : <str>, "price" : <double>, "graph" : <str file name>...}
                              A dictionary of the information we want.
    """

    # Do not put a lot of code here, should mainly be calling helper functions

    # should kind of work on something like this:
    dict = pull_data(stock)
    #img = plot(dict[list_of_prices_or_whatever])
    #file_name = "foo.jpg"
    #save_to_file(img, file_name)
    return dict

    # if apis have graphs and we don't need to plot things ourselves then we
    # can just put all the codes from pull_data() here and no helper functions needed

def pull_data(stockName : str):
    '''
    pull_data

    args:
        str stockName, a ticker for the security

    returns a dictionary regarding info on a stock with ticker stockName

    returns an empty dictionary if the stock ticker doesn't exist

    There is a wait time on this function as it is using the wrapper API
    so we should keep that in mind....


    '''
    stockInfo = yf.Ticker(stockName.upper()).info

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

# worry about these later . . .
def plot(data):
    pass
    # plots the data

def save_to_file(content, file_name):
    pass
    #save things to file given a file name
