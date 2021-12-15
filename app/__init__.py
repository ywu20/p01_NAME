# Team Name -- Yuqing Wu, Andrew Juang, Patrick Ging, Eliza Knapp
# SoftDev
# P01 -- ArRESTed Development
# 2021-12-07

# 12/12 Eliza set up flask for my stock and buy sell pages using backend functions in stock.py

from os import urandom
from flask import Flask, render_template, request, session, redirect, url_for
import user
import stock
import api
import mplfinance as fplt
import pandas as pd
from datetime import datetime
import yfinance as yf

# DO NOT CHANGE THIS
import matplotlib
matplotlib.use('Agg')
# end of do not change - housekeeping


app = Flask(__name__)

app.secret_key = urandom(32)


@app.route("/", methods=['GET', 'POST'])
def index():
    ''' Display login page if there is no username in session, else display the
       response with the session username passed in. '''

    # Renders response if there is a user logged in, else render login page
    if 'username' not in session:
        return render_template('login.html')
    return render_template("dashboard.html", username=session['username'])


@app.route("/auth", methods=['GET','POST'])
def authenticate():
    ''' Checks whether method is get, post. If get method, then redirect to
       loginpage. If post, then authenticate the username and password, rendering
       the error page if incorrect and the response.html if correct username/pass. '''

    # Variables
    method = request.method
    username = request.form.get('username')
    password = request.form.get('password')

    # Get vs Post
    if method == 'GET':
        return redirect(url_for('index'))

    auth_state = user.auth_user(username, password)
    if auth_state == True:
        session['username'] = username
        return redirect(url_for('index'))
    elif auth_state == "bad_pass":
        return render_template('login.html', input="bad_pass")
    elif auth_state == "bad_user":
        return render_template('login.html', input="bad_user")


@app.route("/register", methods=['GET', 'POST'])
def register():
    ''' Displays register page '''

    return render_template('register.html')


@app.route("/rAuth", methods =['GET', 'POST'])
def rAuthenticate():
    ''' Authentication of username and passwords given in register page from user '''

    method = request.method
    username = request.form.get('username')
    password0 = request.form.get('password0')
    password1 = request.form.get('password1')

    if method == 'GET':
        return redirect(url_for('register'))

    if method == 'POST':
        # error when no username is inputted
        if len(username) == 0:
            return render_template('register.html', given = "username")
        # error when no password is inputted
        elif len(password0) == 0:
            return render_template('register.html', given = "password")
        # a username and password is inputted
        # a username and password is inputted
        else:
            # if the 2 passwords given don't match, will display error saying so
            if password0 != password1:
                return render_template('register.html', mismatch = True)
            else:
                user.create_db()
                stock.create_db()
                # creates user account b/c no fails
                if user.create_user(username, password0, 10000, 10000):
                    return render_template('login.html', input='success')
                # does not create account because create_user failed (username is taken)
                else:
                    return render_template('register.html', taken = True)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    ''' Displays currently logged in user's dashboard '''
   # Renders response if there is a user logged in, else render login page
    if 'username' not in session:
        return render_template('login.html')

    return render_template('dashboard.html', username=session['username'])


@app.route("/leaderboard", methods=['GET', 'POST'])
def leaderboard():
    ''' Displays the leaderboard '''

   # Renders response if there is a user logged in, else render login page
    if 'username' not in session:
        return render_template('login.html')

    return render_template('leaderboard.html', username=session['username'])


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    ''' Logout user by deleting user from session dict. Redirects to loginpage '''

    # Delete user. This try... except... block prevent an error from ocurring when the logout page is accessed from the login page
    try:
        session.pop('username')
    except KeyError:
        return redirect(url_for('index'))
    # Redirect to login page
    return redirect(url_for('index'))

@app.route("/manage_stocks", methods=['GET', 'POST'])
def manage_stocks():
    '''
        This is going to allow you to look at your stocks in more detail and also sell shares of them
    '''
   # Renders response if there is a user logged in, else render login page
    if 'username' not in session:
        return render_template('login.html')

    return render_template('manage_stocks.html')

@app.route("/buy_stocks", methods=['GET', 'POST'])
def buy_stocks():
    '''
        This is going to allow you to search up stocks and later it will give you random stocks
        to look at. You can click on them for more info and choose to buy some amount of shares.
    '''
    # Renders response if there is a user logged in, else render login page
    if 'username' not in session:
        return render_template('login.html')

    return render_template("buy_stocks.html", stock=False)

@app.route("/render_image", methods=['GET','POST'])
def render_image():
    args = {
        "ticker" : "MRNA",
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
    imghref = f'static/temp/{args["ticker"]}_from_{startDate}_to_{endDate}.png'
    return render_template("buy_stocks.html", stock=False, img = imghref)

@app.route("/search", methods=['GET', 'POST'])
def search():
    # Renders response if there is a user logged in, else render login page
    if 'username' not in session:
        return render_template('login.html')

    if (request.method == "POST"):
        query = request.form.get("search")

    info = api.pull_data(query)
    if (not info):
        return render_template("buy_stocks.html", stock=False,error="no such stock")

    print(info)
    name = info['officialName']
    price = info['price']
    website = info['website']

    return render_template("buy_stocks.html", symbol=query,stock=True,stock_name=name, stock_price=price, stock_website=website, search = query)

@app.route("/buy_share", methods=['GET', 'POST'])
def buy_share():
    if 'username' not in session:
        return render_template('login.html')

    message = ""
    if (request.method == "POST"):
        requested_shares = request.form.get("num_shares")
        message = str(requested_shares) + " stock shares purchased!"
        print(message)
        price = request.form.get("price")
        print(price)
        stock_symbol = request.form.get("symbol")
        print(stock_symbol)

    change_price = float(price) * int(requested_shares)
    error = stock.buy_sell(session['username'], str(stock_symbol), int(requested_shares))
    # cash decreases
    if (user.update_cash(session['username'], -1 * change_price)):
        # net worth increases
        user.update_networth(session['username'], change_price)
    return render_template("buy_stocks.html", error=message)

if __name__ == "__main__":
    app.debug = True
    app.run()
