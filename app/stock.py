# Team Name -- Yuqing Wu, Andrew Juang, Patrick Ging, Eliza Knapp
# SoftDev
# P01 -- ArRESTed Development
# 2021-12-10

# set up stock database table
import sqlite3
import api
import user
DB_FILE = "discobandit.db"

# 12/11 Andrew do calculate_balance(), finish early so the other things can come together
# 12/12 Eliza finish get_stock function to match what you want with flask displaying
def create_db():
    ''' Creates / Connects to DB File '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS stock_info (user TEXT, stock TEXT, shares INTEGER);")
    db.commit()
    db.close()

def buy_sell(username, stock, amount):
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
    # update_cash for user
    data = api.update_data(stock)
    # print(data)

    price = data["price"] * amount

    # cash update will be in place after Andrew finishes update_cash in the user file
    #if(user.update_cash(-1*price) == False):
    #    return "Does not have enough money to buy stocks"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    # dict for passing into sql
    dict = {"user":username, "stock":stock, "shares":0}

    # get user's stocks
    c.execute("SELECT stock FROM stock_info WHERE user = :user AND stock = :stock", dict)
    exist = c.fetchall()
    print(exist)

    if (exist == []):
        # if stock buying does not exist, add to database
        c.execute("INSERT INTO stock_info VALUES(?,?,?)", (username, stock, amount))
        print("Stock "+stock+ " added.")

    else:
        # if exist add amount
        # get existing shares
        c.execute("SELECT shares FROM stock_info WHERE user = :user AND stock = :stock", dict)
        shares = c.fetchall()
        # print(shares)
        dict["shares"] = shares[0][0] + amount
        c.execute("UPDATE stock_info SET shares = :shares WHERE stock = :stock AND user = :user", dict)
    # if stock selling is 0, delete from database
    c.execute("SELECT shares FROM stock_info WHERE user = :user AND stock = :stock", dict)
    shares = c.fetchall()
    if(shares[0][0]< 0):
        return "Does not have enough shares to sell stocks"
    if (shares[0][0] == 0):
        c.execute("DELETE FROM stock_info WHERE user=:user AND stock = :stock", dict)
        print("stock "+stock+" deleted from database because all shares are sold")

    # add calculate balance once that's done
    db.commit()
    db.close()

def calculate_balance(username):
    """
    Calculates and updates the balance of a user based on the stocks the user owns.
        parameters (str): user to calculate
        returns (double): balance of user
    """

    # calculate balance based on stock owned
    # update balance for user by calling update_balance
    # Andrew do this

def get_stock(username):
    """
    Gets all the the user's stocks, shares, and values of those shares
        paramters (str): user to get
        returns (list): [[stock1, share1, value1], [stock2, share2, value2], ...]
    """
    # get stocks and shares
    # calculate values with update_data to get latest prices
    #(make sure you pip install requirements.txt in repo because pat did yfinance library)
    # Eliza

# for testing ########
create_db()
buy_sell("user1", "AAPL", 10)
buy_sell("user1", "GOOG", 10)
buy_sell("user1", "AMZN", 10)
