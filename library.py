# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:05:55 2019

@author: Paul J
"""

import requests # libary api request
import json # libary data standardization
import sqlite3 # libary SQlite
import random # libary random numbers

### Connect to SQlite database  ###
conn = sqlite3.connect('Currency.db')  # Connection to data base
c = conn.cursor() # save pointer 
c.execute('CREATE TABLE if not exists CURRENCY_Table ([date] text PRIMARY KEY, [GBP] float, [USD] float)') # create table 