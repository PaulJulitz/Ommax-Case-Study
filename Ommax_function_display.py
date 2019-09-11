# -*- coding: utf-8 -*-

from library import *

import Ommax_function_load as ofl
           
def show():
    data = ofl.load()
    
    for h in data: # Check if data is the same
        sql_date = h[0]
        sql_gbp_rate = h[1]
        sql_usd_rate = h[2]
        print("On " +  sql_date + " 1 EUR equals " + str(sql_gbp_rate)+ " GBP, and " + str(sql_usd_rate)+ " USD.")