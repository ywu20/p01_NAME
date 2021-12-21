#Name — Andrew Juang, Eliza Knapp, Patrick Ging, Yuqing Wu
#Softdev
#P01: ArRESTed Development
#2021-12-10

import requests, urllib, json

def get_fact():
  try:
    r = urllib.request.urlopen("https://asli-fun-fact-api.herokuapp.com/")
    JSON = r.read()
    info = json.loads(JSON)['data']
    fact = info['fact']
    return fact
  except:
    print("error finding the api")
    return "error finding the api"

def numbers(num):
    try:
        r = urllib.request.urlopen("http://numbersapi.com/" + str(num))
        fact = r.read().decode('UTF-8')
        return fact
    except:
        print("numbers api failed.")
        return "error"
