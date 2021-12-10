# Team Name -- Yuqing Wu, Andrew Juang, Patrick Ging, Eliza Knapp
# SoftDev
# P01 -- ArRESTed Development
# 2021-12-10

# set up stock database table
import sqlite3
DB_FILE = "discobandit.db"

def create_db():
    ''' Creates / Connects to DB File '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS stock_info (username TEXT, stock TEXT, shares INTEGER);")
    db.commit()
    db.close()

def buy_sell(user, stock, amount):
    """
    Buys and sells stock for user
        parameters (str, int, str): stock name / symbol
                                    amount to buy: + for an actual buy action, - for a sell action
                                    user who's buying/selling the stock
        returns (boolean): true for success, false for fail
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    # if stock buying does not exist, add to database
    c.execute("INSERT INTO stock_info VALUES(?,?,?)", (user, stock, amount))
    # if stock selling is 0, delete from database
    # if exist add amount
    # update_cash for user
    # Yuqing will do
    db.commit()
    db.close()

def calculate_balance(user):
    """
    Calculates and updates the balance of a user based on the stocks the user owns.
        parameters (str): user to calculate
        returns (double): balance of user
    """

    # calculate balance based on stock owned
    # update balance for user by calling update_balance
    # Andrew do this

def get_stock(user):
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
buy_sell("user1", "APPL", 10)
