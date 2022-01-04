# Team Name -- Yuqing Wu, Andrew Juang, Patrick Ging, Eliza Knapp
# SoftDev
# P01 -- ArRESTed Development
# 2021-12-10

# set up stock database table
import sqlite3
import api
import user
DB_FILE = "discobandit.db"


def create_db():
    ''' Creates / Connects to DB File '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS stock_info (user TEXT, stock TEXT, shares INTEGER);")
    db.commit()

def buy_sell(username, stock, amount, price_one):
    """
    Buys and sells stock for user
        parameters (str, int, str): stock name / symbol
                                    amount to buy: + for an actual buy action, - for a sell action
                                    user who's buying/selling the stock
        returns (str): error messages
                        Success!
                        Does not have enough money to buy stocks
                        Does not have enough shares to sell stocks
    This function does not yet safe guard against the situation where user sells stocks that
    they don't own but the flask and html should make the user impossible to sell anything they don't have

    Also assumes stocks exists because through the search function the user should only be allowed
    to buy & sell stocks once the search exists
    """

    price = price_one * amount

    # cash update will be in place after Andrew finishes update_cash in the user file
    if(user.update_cash(username, -1*price) == False):
        return "Does not have enough money to buy stocks"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    # dict for passing into sql
    dict = {"user":username, "stock":stock, "shares":0}

    # get user's stocks
    c.execute("SELECT stock FROM stock_info WHERE user = :user AND stock = :stock", dict)
    exist = c.fetchall()

    if (exist == []):
        # if stock buying does not exist, add to database
        c.execute("INSERT INTO stock_info VALUES(?,?,?)", (username, stock, amount))

    else:
        # if exist add amount
        # get existing shares
        c.execute("SELECT shares FROM stock_info WHERE user = :user AND stock = :stock", dict)
        shares = c.fetchall()
        dict["shares"] = shares[0][0] + amount
        c.execute("UPDATE stock_info SET shares = :shares WHERE stock = :stock AND user = :user", dict)
    # if stock selling is 0, delete from database
    c.execute("SELECT shares FROM stock_info WHERE user = :user AND stock = :stock", dict)
    shares = c.fetchall()
    if(shares[0][0]< 0):
        return "Does not have enough shares to sell stocks"
    if (shares[0][0] == 0):
        c.execute("DELETE FROM stock_info WHERE user=:user AND stock = :stock", dict)

    db.commit()
    return "Success!"

def calculate_networth(username, stocks):
    """
    Calculates and updates the balance of a user based on the stocks the user owns.
        parameters (str): user to calculate
                    (list): what get_stock returns, is only called in get_stock

        returns (float): balance of user
    """

    networth = user.get_cash(username)
    for i in stocks:
        networth+= i[2]

    # update networth for user by calling update_networth in user
    user.update_networth(username,networth)
    return float(networth)


def get_stock(username):
    """
    Gets all the the user's stocks, shares, and values of those shares
        paramters (str): user to get
        returns (list): [[stock1, share1, value1], [stock2, share2, value2], ...]
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    # get stocks and shares
    output_list = []
    c.execute("SELECT stock,shares FROM stock_info WHERE user = :user", {"user":username})
    list = c.fetchall()
    for i in list:
        li = [i[0], i[1]]
        # calculate values with update_data to get latest prices
        var = api.update_data(li[0])["price"]
        li.append(var * li[1])
        li.append(var)
        output_list.append(li)
    calculate_networth(username, output_list)
    return output_list

def get_shares_of_stock(username, stock):
    '''
    returns the number of shares of a specific stock a user has (using the symbol)
    '''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT shares FROM stock_info WHERE user = (?) AND stock = (?)", (username, stock))
    list = c.fetchall()
    return list[0][0]
