# Team Name -- Yuqing Wu, Andrew Juang, Patrick Ging, Eliza Knapp
# SoftDev
# P01 -- ArRESTed Development
# 2021-12-07

from os import urandom
from flask import Flask, render_template, request, session, redirect, url_for
import user
import stock
import api
import graph
import fun_facts
import cryptoData
import random
import news

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
    stocks = stock.get_stock(session['username'])
    networth = user.get_networth(session['username'])
    cash = user.get_cash(session['username'])

    num_fact = ""
    rand_num = 0
    lottery = False
    success = False
    if request.method == 'POST' and request.form.get("lottery") == "Lottery":
        lottery = True
        rand_num = random.randint(-100, 100)
        num_fact = fun_facts.numbers(abs(rand_num))
        user.update_cash(session['username'],rand_num)
        user.update_networth(session['username'], user.get_networth(session['username']) + rand_num)
        if rand_num >= 0:
            success = True

    return render_template('dashboard.html', username=session['username'],
                                             stocks = stocks,
                                             networth = round(float(networth),2),
                                             cash = round(float(cash),2),
                                             num_fact = num_fact,
                                             lottery = lottery,
                                             rand_num = abs(rand_num),
                                             success = success,
                                             isBroke = user.get_networth(session['username']) < 100  #if they're broke we'll give them the option to reset :)
                                             )


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



@app.route("/resetAccount", methods=["GET", "POST"])
def resetAccount():
    if 'username' not in session:
        return render_template('login.html')

    for item in stock.get_stock(session['username']):
        stock.buy_sell(session['username'], item[1], item[2]) # selling stocks

    user.update_cash(session['username'], -1 * user.get_cash(session['username'])) #clearing cash

    user.update_cash(session['username'], 10000) #adding 10k

    return redirect("/")


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


@app.route("/dashboard/<username>", methods=['GET', 'POST'])
def dashboard(username):
    ''' Displays currently logged in user's dashboard '''
   # Renders response if there is a user logged in, else render login page
    stocks = stock.get_stock(username)
    networth = user.get_networth(username)
    cash = user.get_cash(username)

    return render_template('others.html', username=username,
                                             stocks = stocks,
                                             networth = round(float(networth),2),
                                             cash = round(float(cash), 2)
                                             )



@app.route("/leaderboard", methods=['GET', 'POST'])
def leaderboard():
    ''' Displays the leaderboard '''

   # Renders response if there is a user logged in, else render login page
    if 'username' not in session:
        return render_template('login.html')

    leaderboard = user.fetch_leaderboard()

    return render_template('leaderboard.html', username=session['username'], leaderboard=enumerate(leaderboard))


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

    # the networth and cash don't align yet because updating timing not right, fixing database to include a new column of prices.
    stocks = stock.get_stock(session['username'])
    networth = user.get_networth(session['username'])
    cash = user.get_cash(session['username'])
    return render_template('manage_stocks.html', stocks = stocks, networth = round(float(networth),2), cash = round(float(cash),2))


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


@app.route("/search", methods=['GET', 'POST'])
def search():
    '''
        klsdjffd
    '''
    # Renders response if there is a user logged in, else render login page
    if 'username' not in session:
        return render_template('login.html')

    if request.method == "GET":
        return redirect("/buy_stocks")

    if (request.method == "POST"):
        query = request.form.get("search").lower()


    info = api.update_data(query)

    if (not info):
        #two possibilities, it's a cryptocurrency or it's something that we don't have
        info = cryptoData.getTodayInfo(query)
        try:
            if info.get("error") is not None:
                return render_template("buy_stocks.html", stock=False, error="no such stock")
        except:
            return render_template("buy_stocks.html", stock=False, error="no stock avaliable at this time")

        symbol = ""
        stock_price = ""
        stock_name = ""
        stock_website = ""

        try:
            symbol = info["symbol"]
            stock_price = info["market_data"]['current_price']['usd']
            stock_name = info['name']
            stock_website= f'https://www.coingecko.com/en/coins/{query}'
        except:
            return render_template("buy_stocks.html", stock=False, error="no such info on that stock")

        else:
            return render_template("buy_stocks.html",
                symbol=symbol,
                stock=True,
                stock_price=stock_price,
                stock_name=stock_name,
                stock_website= stock_website,
                search = query,
                img = cryptoData.getOHLC(query),
                isCrypto=True,
                news=news.grabByTicker(query))
    # get image href
    try:
        imghref = graph.get_graph_href(query)
    except:
        print("did not find graph") # just in case

    name = ""
    price = ""
    website = ""

    try:
        name = info['officialName']
        price = info['price']
        website = info['website']
    except:
        render_template("buy_stocks.html", stock = False, error= "stock error")


    return render_template("buy_stocks.html", symbol=query,
                                              stock=True,
                                              stock_name=name,
                                              stock_price=price,
                                              stock_website=website,
                                              search = query,
                                              img = imghref,
                                              isCrypto = False,
                                              news=news.grabByTicker(query)
                                              )


@app.route("/buy_share", methods=['GET', 'POST'])
def buy_share():
    if 'username' not in session:
        return render_template('login.html')

    message = ""
    if (request.method == "POST"):
        requested_shares = request.form.get("num_shares")
        price = request.form.get("price")
        stock_symbol = request.form.get("symbol")

    # change_price = float(price) * int(requested_shares)
    error=""
    if (int(requested_shares) <= 0):
        error = "Share number cannot be less than or equal to 0"
    else:
        error = stock.buy_sell(session['username'], str(stock_symbol), int(requested_shares), float(price))

    return render_template("buy_stocks.html", error=str(error))

@app.route("/sell_share", methods=['GET', 'POST'])
def sell_share():
    if 'username' not in session:
        return render_template('login.html')

    stock_symbol = request.form.get("symbol")
    shares = stock.get_shares_of_stock(session['username'], stock_symbol)

    return render_template("sell_stock.html", symbol=stock_symbol, shares = shares, price=round(float(request.form.get("price")), 2))

@app.route("/handle_sell_share", methods=['GET', 'POST'])
def handle_sell_share():
    if 'username' not in session:
        return render_template('login.html')
    '''
    THEN- there's a different function that takes the number of shares
    bought and handles it (stock.buy_sell)
    '''
    shares = int(request.form.get("num_shares"))
    error = ""
    if (shares <= 0):
        error = "Share number cannot be less than or equal to 0"
    else:
        error = stock.buy_sell(session['username'], request.form.get("symbol"), -1 * shares, float(request.form.get("price")))
    # update ALL of the data again just to make sure!
    stocks = stock.get_stock(session['username'])
    networth = user.get_networth(session['username'])
    cash = user.get_cash(session['username'])

    message = "You completed a transaction: " + str(error)

    return render_template('manage_stocks.html', stocks = stocks, networth = round(float(networth),2), cash = round(float(cash), 2), error= message)

if __name__ == "__main__":
    app.debug = True
    app.run()
