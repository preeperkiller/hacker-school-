#HIER
#|
#|
#V
from tkinter import *
import webbrowser
import requests

root=Tk()
root.title("Suchleiste")
root.geometry("400x200")


label1=Label(root,text="Enter URL here :",font=("arial",10,"bold"))
label1.grid(row=0,column=0)


label2=Label(root,text="Enter Subject here :",font=("arial",10,"bold"))
label2.grid(row=5,column=0)


entry1=Entry(root,width=30)
entry1.grid(row=2,column=0)

entry2=Entry(root,width=30)
entry2.grid(row=7,column=0)

def Suche():
    print('hi')
    #Für debug : Coder von Gestern
    #from bs4 import BeautifulSoup
    import requests
    #import timeit

    url = entry1.get()
    suche = entry2.get()

    def get_url_content(url):
        return requests.get(url).text

    print(get_url_content(url))
    print(type(get_url_content(url)))

    data = get_url_content(url)


    

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



#Suche()   
button=Button(root,text="Suche", command=Suche)
button.grid(row=20,column=0,columnspan=2,pady=10) 



root.mainloop()
