# -*- coding: utf-8 -*-

from library import random

import Ommax_function_load as ofl
import Ommax_function_extrator as ofe

def check():
    data = ofl.load()
    g = []
    for x in range(5):
       c = random.choice(data)
       data.remove(c) # Extract one element of the set
       g.append(c) # Saves the extraced element
    
    for h in g: # Check if data is the same
        datum = h[0]
        y,m,d = datum.split('-')
        aus = ofe.extrator(d, y, m)
        if aus != h:
           print('SQlite data for '+ datum +' is INCORRECT.')
        else:
         print('SQlite data for '+ datum +' is correct.')
