#Name — Andrew Juang, Eliza Knapp, Patrick Ging, Yuqing Wu
#Softdev
#P01: ArRESTed Development
#2021-12-10

import sqlite3

# 12/11 Andrew do update_balance, update_cash, get_balance, get_cash
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
# def update_cash(amount):
    """
    updates the amount of cash the user has
    if the amount the user want to spend is
        greater than what they currently have,
        returns false, does not change the amount
        of cash, otherwise update and return true
            parameters (double): amount to be update by
            returns (boolean): true success, false fail
    """

# def update_balance(amount):
    """
    updates the balance of the user
        parameters (double): amount to change by
        returns: None
    """

# def get_cash(user):
    """
    gets the amount of cash a user has
        parameters (str): user to get
        returns (double): user's cash
    """

# def get_balance(user):
    """
    gets the balance of a user
        parameters (str): user to get
        returns (double): user's balance
    """
# Functions to be done later .  . .
# def leaderboard():
#
# def percent_lost():


# For testing purposes #################
create_db()
