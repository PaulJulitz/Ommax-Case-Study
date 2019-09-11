# -*- coding: utf-8 -*-

from library import c

import Ommax_function_extractor as ofe

def save():
    for i in range(1,31):
        if i < 10: # Data format: 0x or yx 
            i = "0"+str(i)
        else:
            i = str(i)
        data = ofe.extractor(i) # Push data

        try: # Ignore Error Message; Alternative clear database: DROP TABLE Statement
            a = 'insert into CURRENCY_Table values ("{}",{},{})'.format(*data) # Pointer to data
#           a = 'insert into CURRENCY_Table values ("{}",{},{})'.format(date, gbp_rate, usd_rate)
            c.execute(a) # Save in data base
  
        except Exception as e: # Exception writes error message into e
#           print(e) # Check of error message 
            pass 
