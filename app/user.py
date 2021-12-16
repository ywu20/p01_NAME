#Name — Andrew Juang, Eliza Knapp, Patrick Ging, Yuqing Wu
#Softdev
#P01: ArRESTed Development
#2021-12-10

import sqlite3

DB_FILE = "discobandit.db"

def create_db():
    ''' Creates / Connects to DB File '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS users (usernames TEXT, passwords TEXT, cash REAL, networth REAL);")
    db.close()


def auth_user(username, password):
    ''' Validates a username + password when person logs in '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS users (usernames TEXT, passwords TEXT, cash REAL, networth REAL);")
    # Create List of Users
    c.execute("SELECT usernames FROM users")
    users = []
    for a_tuple in c.fetchall():
        users.append(a_tuple[0])

    if username in users:
        c.execute("SELECT passwords FROM users WHERE usernames = '" + username + "'")
        if c.fetchall()[0][0] == password:
            return True
        else:
            return "bad_pass"
    else:
        return "bad_user"


def create_user(username, password, cash, networth):
    ''' Adds user to database if right username and password are given when a
        person registers '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    # Create List of Users
    c.execute("SELECT usernames FROM users")
    users = []
    for a_tuple in c.fetchall():
        users.append(a_tuple[0])

    # username is not taken, creates account with given username and password
    if username in users:
        return False
    else:
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?);", (username, password, cash, networth))
        db.commit()
        return True


def get_cash(user):
    """
    gets the amount of cash a user has
        parameters (str): user to get
        returns (double): user's cash
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT cash FROM users WHERE usernames = '" + user + "'")
    return float(c.fetchall()[0][0])


def update_cash(user, amount):
    """
    updates the amount of cash the user has if the amount the user want to spend is
    greater than what they currently have, returns false, does not change the amount
    of cash, otherwise update and return true
        parameters (double): amount to be update by
        returns (boolean): true success, false fail
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    amount = get_cash(user) + amount
    if amount < 0:
        return False
    else:
        amount = str(amount)
        c.execute("UPDATE users SET cash ='" + amount + "' WHERE usernames = '" + user + "'")
        db.commit()
        return True


def get_networth(user):
    """
    gets the networth of a user
        parameters (str): user to get
        returns (double): user's balance
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("SELECT networth FROM users WHERE usernames = '" + user + "'")
    return float(c.fetchall()[0][0])


def update_networth(user, amount):
    """
    updates the balance of the user
        parameters (double): amount to change by
        returns: None
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    amount = str(amount)
    c.execute("UPDATE users SET networth ='" + amount + "' WHERE usernames = '" + user + "'")
    db.commit()
    #db.close()

def fetch_leaderboard():
    ''' Fetch list of users sorted by networth '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM users")

    leaderboard = []
    for a_tuple in c.fetchall():
        networth = a_tuple[3]
        user = a_tuple[0]
        leaderboard.append((networth, user))

    leaderboard.sort()

    return leaderboard


# Functions to be done later .  . .
# def leaderboard():
#
# def percent_lost():


# For testing purposes #################
#create_db()
#create_user("andrew", "01", 1000, 1000)
#print(get_cash("andrew"))
#print(get_networth("andrew"))
#if update_cash("andrew", -100000.0):
#    print(get_cash("andrew"))
#print(get_cash("andrew"))
#update_networth("andrew",10)
#print(get_networth("andrew"))
fetch_leaderboard()
