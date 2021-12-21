#Name — Andrew Juang, Eliza Knapp, Patrick Ging, Yuqing Wu
#Softdev
#P01: ArRESTed Development
#2021-12-10

import requests, urllib, json

def get_fact():
  r = urllib.request.urlopen("https://asli-fun-fact-api.herokuapp.com/")
  JSON = r.read()
  info = json.loads(JSON)['data']
  fact = info['fact']
  return fact

# print(get_fact())
