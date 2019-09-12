# -*- coding: utf-8 -*-

import Ommax_function_load as ofl
           
def display():
    data = ofl.load()
    
    for h in data: # Check if data is the same
        sql_date = h[0]
        sql_gbp_rate = h[1]
        sql_usd_rate = h[2]
        print(f'On {sql_date} 1 EUR equals {sql_gbp_rate} GBP, and {sql_usd_rate} USD.')