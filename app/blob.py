import sqlite3
import yfinance as yf
import requests
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import json
import time
import datetime

DB_FILE = "discobandit.db"
TABLENAME = "imageDB"

class ImageTable:
    def __init__(self, tableName : str, fileName : str):
        '''
        __init__
            args:
                self
                tableName : str, a string for the name of the table
                fileName : str, a string for the name of the db file
        '''
        self._db = sqlite3.connect(fileName)
        self._cursor = self._db.cursor()

        self._cursor.execute(f"CREATE TABLE IF NOT EXISTS {tableName} (id INTEGER PRIMARY KEY);")
        self._db.close()

    def addPriceImage(self, args):
        '''
        {
            symbol : ticker,
            resolution : "D",
            fromYear : year,
            fromMonth : year,
            fromDay : year,
            toYear : year,
            toMonth : year,
            toDay : year

        }

        '''
        #why do this? because it's just easier to use near the __init__ file
        newArgs = {
            "symbol" : args["ticker"],
            "resolution" : args["resolution"],
            "from" : int( time.mktime(datetime.datetime(
                args["fromYear"],
                args["fromMonth"],
                args["fromDay"]
            ).timetuple())) ,
            "to" : int( time.mktime(datetime.datetime(
                args["toYear"],
                args["toMonth"],
                args["toDay"]
            ).timetuple())),
            "token" : args["token"]
            }
            
        stockData = requests.get("https://finnhub.io/api/v1/stock/candle?", params=newArgs).json()

        '''
        insert matplotlib stuff to generate the function, for now it'll just return the data
        '''

        return stockData

###### TESTING ######################
x = ImageTable(TABLENAME, DB_FILE)
print(x.addPriceImage({
    "ticker" : "AAPL",
    "resolution" : "D",
    "fromYear" : 2021,
    "fromMonth" : 12,
    "fromDay" : 9,
    "toYear" : 2021,
    "toMonth" : 12,
    "toDay" : 9,
    "token" : "c6qgpm2ad3i891nj4g5g"
    })
)
