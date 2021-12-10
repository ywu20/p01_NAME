# Team Name -- Yuqing Wu, Andrew Juang, Patrick Ging, Eliza Knapp
# SoftDev
# P01 -- ArRESTed Development
# 2021-12-10

# set up stock database table

def buy_sell(stock, amount, user):
    """
    Buys and sells stock for user
        parameters (str, int, str): stock name / symbol
                                    amount to buy: + for an actual buy action, - for a sell action
                                    user who's buying/selling the stock
        returns (boolean): true for success, false for fail
    """

    # if stock buying does not exist, add to database
    # if stock selling is 0, delete from database
    # if exist add amount
    # update_cash for user
    # Yuqing will do

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
    # calculate values
