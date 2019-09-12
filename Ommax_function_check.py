# -*- coding: utf-8 -*-

from library import random

import Ommax_function_load as ofl
import Ommax_function_extractor as ofe

def check():
    data = ofl.load() # List
    choice = [] # 
    for x in range(5):
       c = random.choice(data)
       data.remove(c) # Extract one element of the set
       choice.append(c) # Saves the extracted element
    
    for h in choice: # Check if data is the same
        datum = h[0]
        y,m,d = datum.split('-')
        aus = ofe.extractor(d, y, m)
        if aus != h:
           print('SQlite data for '+ datum +' is INCORRECT.')
        else:
         print('SQlite data for '+ datum +' is correct.')