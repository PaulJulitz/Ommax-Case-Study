# -*- coding: utf-8 -*-

#############################################
#   Python 3.6 Application: Ommax Case Study
#############################################

from library import conn

# Load only what you need: conn, c, requests, json, sqlite3, random
# Load everything: *

import Ommax_function_save as ofs
import Ommax_function_check as ofc
import Ommax_function_display as ofd

### Execute Application ###
print("Python 3.6 Application: Currentcy Rates from 01.09.2018 untill 30.09.2018")
print('')
print('1. Fetch Data form Fixer API, and save Data to SQlite Database ... ')
print(' ... ')
ofs.save()
print('')
print('2. SQlite Database holds the following valus:')
ofd.show()
print('')
print("3. Check if five random entries in SQlite database are correct.")
ofc.check()

conn.commit() # Open up connection to data base


