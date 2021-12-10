#Name — Andrew Juang, Eliza Knapp, Patrick Ging, Yuqing Wu
#Softdev
#P01: ArRESTed Development
#2021-12-10


def update_data(stock):
    """
    Gets the newest data for a stock
        parameter (str): symbol / name (depending on which one the apis use
               to identify the stock )of the stock we want data for.
        returns (dictionary): {"name / symbol" : <str>, "price" : <double>, "graph" : <str file name>...}
                              A dictionary of the information we want.
    """

    # Do not put a lot of code here, should mainly be calling helper functions

    # should kind of work on something like this:
    #dict = pull_data(stock)
    #img = plot(dict[list_of_prices_or_whatever])
    #file_name = "foo.jpg"
    #save_to_file(img, file_name)
    #return dict

    # if apis have graphs and we don't need to plot things ourselves then we
    # can just put all the codes from pull_data() here and no helper functions needed

# 12/10 get this done - make sure that the current prices of the stock is getable first
# Pat
def pull_data(stock):
    # get api with keys and stuff
    # returns the information we need in  a dictionary

# worry about these later . . .
def plot(data):
    # plots the data

def save_to_file(content, file_name):
    #save things to file given a file name
