# how-to :: Install the Yahoo Finance API Wrapper for Python3
---
## Overview
Some of you guys might need to create a graph stock data, market data, etc. There are many services for it, but they're marred by quotas and oftentimes unclear documentation. MPL finance makes this coding experience much much easier.  
### Estimated Time Cost: 5-10 minutes 

### Prerequisites:

- Have pip installed on your computer 
- Have Python3 working on your computer
- Have an internet connection on your computer

1. Open your terminal and verify you have pip3 and python3. You can verify this by typing
 ```python3``` or ```pip3``` on your computer and awaiting a response. If this step fails then troubleshoot and ensure the two are working.
2. Once verified, you can then type in ```pip3 install mplfinance``` or if ```pip``` is your pip3 command keyword (for some reason that's the case for me on my windows computer) type ```pip install yfinance```
3. It will take a bit of time because it will be installing dependencies for the yfinance library if you don't already have them installed. This could take a while depending on your internet connection so wait for it to complete.
4. Make sure yfinance was installed sucessfully. You can verify this by typing ```python3``` in your terminal and typing in ```import mplfinance```. If it installed correctly, you shouldn't get any errors. If it does fail, check you're using the right python and ensure you installed it onto your venv or right place.
5. There you go! You have successfully installed it. You can learn more about its functionalities through the resources below!  
### Resources
*

---
## Making the image

The main way we access stock information in the mpl module is with the Ticker object.

To access data about a particular stock use the Ticker constructor with the ticker name as the argument
```
import yfinance as yf

apple = yf.Ticker("AAPL")
# ^^^ constructor for apple ticker  
````

You can do a plethora of things with this ticker object - below are a few examples. All of this comes from the documentation provided in the second link. 

```
import yfinance as yf

apple = yf.Ticker("AAPL")

#get basic info
#returns a dictionary of info about stock like business summary, current price, the company's official name etc.
apple.info 

apple.info["longBusinessSummary"]
apple.info["currentPrice"]

#show dividends
#use the date the dividends are distributed as the key, shows amount of dividends
apple.dividends

apple.dividends["2021-11-05"]

#news on the stock
#returns a list of dictionaries that contains recent high ranking news information like title, publisher, and link to news
apple.news

apple.news[0]["title"]

#analyst recommendations
#use date as the key. If recommendations are made on that day, provide information about the type of recommendation and the firm that made the recommendation
apple.recommendations
apple.recommendations["2021-10-29"]
```
---

Accurate as of (last update): 2021-12-12

#### Contributors:  
Patrick  Ging  Pd2  
Yuqing Wu Pd2  