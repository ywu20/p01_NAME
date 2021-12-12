# how-to :: Install the Yahoo Finance API Wrapper for Python3
---
## Overview
Some of you guys might need an API to access stock data, market data, etc. There are many services for it, but they're marred by quotas and oftentimes unclear documentation. This wrapper uses the Yahoo Finance API and makes the coding experience much much easier.  
### Estimated Time Cost: 5-10 minutes 

### Prerequisites:

- Have pip installed on your computer 
- Have Python3 working on your computer
- Have an internet connection on your computer

1. Open your terminal and verify you have pip3 and python3. You can verify this by typing
 ```python3``` or ```pip3``` on your computer and awaiting a response. If this step fails then troubleshoot and ensure the two are working.
2. Once verified, you can then type in ```pip3 install yfinance``` or if ```pip``` is your pip3 command keyword (for some reason that's the case for me on my windows computer) type ```pip install yfinance```
3. It will take a bit of time because it will be installing dependencies for the yfinance library if you don't already have them installed. This could take a while depending on your internet connection so wait for it to complete.
4. Make sure yfinance was installed sucessfully. You can verify this by typing ```python3``` in your terminal and typing in ```import yfinance```. If it installed correctly, you shouldn't get any errors. If it does fail, check you're using the right python and ensure you installed it onto your venv or right place.
5. There you go! You have successfully installed it. You can learn more about its functionalities through the resources below!  
### Resources
* https://pypi.org/project/yfinance/
* https://github.com/ranaroussi/yfinance

---
## Intro to the module

The main way we access stock information in the yfinance module is with the Ticker object.

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
#to get specific information
apple.info["longBusinessSummary"]
apple.info["currentPrice"]

#show dividends
apple.dividends

#news on the stock
#returns a list of dictionaries that contains news information like title, publisher, and link to news
apple.news

#analyst recommendations
apple.recommendations

```
---

Accurate as of (last update): 2021-12-12

#### Contributors:  
Patrick  Ging  Pd1
