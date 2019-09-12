# -*- coding: utf-8 -*-

import requests # Library api request
import json # Library data standardization
import sqlite3 # Library SQLite
import random # Library random numbers

### Connect to SQlite database  ###
conn = sqlite3.connect('Currency.db')  # Connection to data base
c = conn.cursor() # Save pointer 
c.execute('CREATE TABLE if not exists CURRENCY_Table ([date] text PRIMARY KEY, [GBP] float, [USD] float)') # create table 