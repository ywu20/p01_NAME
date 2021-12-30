import mplfinance as fplt
import pandas as pd
from datetime import datetime
import yfinance as yf

def get_graph_href(query):
    '''
    will generate a graph of the securities data

    returns the path way to it

    params query, str: the ticker of the security
    if there's an error it will return the error .png
    '''
    try:
        args = {
            "ticker" : query,
            "resolution" : "D",
            "fromYear" : 2021,
            "fromMonth" : 11,
            "fromDay" : 9,
            "toYear" : 2021,
            "toMonth" : 12,
            "toDay" : 11
        }
        startDate = f'{args["fromYear"]}-{args["fromMonth"]}-{args["fromDay"]}'
        endDate = f'{args["toYear"]}-{args["toMonth"]}-{args["toDay"]}'
        # ^^ some strings that'll be useful later

        if args["toYear"] - args["fromYear"] > 2:
            #sometimes there is just so much data that it becomes pointless to try chart a candle
            #this might be remedied in other ways, but I need to sit on it right now
            mode = "line"
        else:
            mode = "candle"
        

        fplt.plot(
                yf.download(
                    args["ticker"],
                    start=startDate ,
                    end=endDate),
                type=mode,
                title=f'{args["ticker"]}, from {startDate} to {endDate}',
                ylabel='Price ($)',
                savefig=f'static/temp/{args["ticker"]}_from_{startDate}_to_{endDate}.png' # for saving the graph
            )
        return f'static/temp/{args["ticker"]}_from_{startDate}_to_{endDate}.png'
    except:
        return 'static/temp/Error.png'
