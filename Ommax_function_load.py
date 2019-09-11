# -*- coding: utf-8 -*-

from library import c
    
def load():
    data = [] # List
    b = 'select * from CURRENCY_Table'
#    b = 'select date, GBP, USD from CURRENCY_Table' # Singel entries
    d = c.execute(b) # Curser pointer (sql curser)
    for i in d: # iterate over object (curser object has the property of an iterator)
       # print(i) Control message 
       data.append(i) # Addend to list 
    return data
