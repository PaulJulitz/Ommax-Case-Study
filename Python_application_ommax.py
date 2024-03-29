# -*- coding: utf-8 -*-

#############################################
#   Python 3.6 Application: OMMAX Case Study
#############################################

from library import conn

# Load only what you need: conn, c, requests, json, sqlite3, random
# Load everything: *

import Ommax_function_save as ofs
import Ommax_function_check as ofc
import Ommax_function_display as ofd

### Execute Application ###
print('#############################################################################')
print('Python 3.6 Application: Fixer Currency Rates from 01.09.2018 until 30.09.2018')
print('')
print('1. Fetch Data form Fixer API and save Data to SQLite Database.')
print(' ... ')
ofs.save()
print('')
print('2. SQLite Database holds the following values:')
ofd.display()
print('')
print('3. Check if five random entries in SQLite database are correct.')
ofc.check()

conn.commit() # Save changes 
conn.close() # Close the connection