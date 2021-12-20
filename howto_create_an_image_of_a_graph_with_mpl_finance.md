# how-to :: Make a graph PNG in MplFinance
---
## Overview
Some of you guys might or may not need to create graph images. Fortunately, we've been through the pain of making it and decided to share it!
### Estimated Time Cost: 15-20 minutes 

### Prerequisites:

- Have pip installed on your computer 
- Have Python3 working on your computer
- Have an internet connection on your computer

### Installing the library:
1. Open your terminal and verify you have pip3 and python3. You can verify this by typing
 ```python3``` or ```pip3``` on your computer and awaiting a response. If this step fails then troubleshoot and ensure the two are working.
2. Once verified, you can then type in ```pip3 install mplfinance``` or if ```pip``` is your pip3 command keyword (for some reason that's the case for me on my windows computer) type ```pip install mplfinance```
3. It will take a bit of time because it will be installing dependencies for the mplfinance library if you don't already have them installed. This could take a while depending on your internet connection so wait for it to complete.
4. Make sure yfinance was installed sucessfully. You can verify this by typing ```python3``` in your terminal and typing in ```import mplfinance```. If it installed correctly, you shouldn't get any errors. If it does fail, check you're using the right python and ensure you installed it onto your venv or right place.

## Making the image

For the purposes of this example, our data will be a pandas dataframe that was obtained using the yfinance module. See our guide on yfinance for more on that!

The first thing you want to do is import mplfinance
```
import mplfinance as fplt
```
When we want to plot a function, we use the fplt.plot() command.  
```
startDate = f'{args["fromYear"]}-{args["fromMonth"]}-{args["fromDay"]}'
endDate = f'{args["toYear"]}-{args["toMonth"]}-{args["toDay"]}'
fplt.plot(
            data_to_plot,
            type=mode,
            title=f'{args["ticker"]}, from {startDate} to {endDate}',
            ylabel='Price ($)',
            savefig=f'static/temp/{args["ticker"]}_from_{startDate}_to_{endDate}.png' # for saving the graph
        )
    
```
One thing that is ESSENTIAL is that you give an argument for savefig. This will tell mplfinance that you want to save it.

ONLY IF YOU'RE USING IT FOR FLASK
```
import matplotlib

# This tells it not to try use the GUI, which will crash flask.

matplotlib.use('Agg')
``` 
---

Accurate as of (last update): 2021-12-12

#### Contributors:  
Patrick  Ging  Pd2  
Andrew Juang Pd2  
