# -*- coding: utf-8 -*-

from library import c
    
def load():
    data = []
    b = 'select * from CURRENCY_Table'
#    b = 'select date, GBP, USD from CURRENCY_Table' # Singel entries
    d = c.execute(b)
    for i in d:
       # print(i) Controll message 
        data.append(i)
    return data

