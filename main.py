#from bs4 import BeautifulSoup
import requests
#import timeit

url = input("Auf welcher Website soll gesucht werden? (In diesem Format: https://seite.de)")

def get_url_content(url):
    return requests.get(url).text

print(get_url_content(url))
print(type(get_url_content(url)))

data = get_url_content(url)


suche = input("Was soll gesucht werden? ")

#print(data.find(suche)) # DEBUG
zeichen = data.find(suche)
#data_ = data[zeichen:]
data_ = data[zeichen:]
zeichen = data.find(suche)

print(data_)
stringliste = ""
habenzahlenangefangen = False
istdanezahl = False
for string in data_:
  print(string)
  
  #try:
  # int(string)
  try:
    int(string)
    stringliste = stringliste + (str(string))
    istdanezahl = True
    habenzahlenangefangen = True
  
  except ValueError:
    if habenzahlenangefangen == True:
      if istdanezahl == False:
        break
    istdanezahl = False

  
  #except:
  #  pass

print("-------------------")
print(stringliste)
#f = open("demofile.html", "w")
#f.write(data)

