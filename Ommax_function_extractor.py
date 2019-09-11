# -*- coding: utf-8 -*-
# ACCESS Key: 8bffd25ad11e370e74c1386a39d8192d
# Username: Augsburg

from library import json, requests

def extractor(day, year= '2018', month='09'):
    url = "http://data.fixer.io/api/" + year + "-" + month + "-" + day # Only variable day
    ACCESS_KEY = "8bffd25ad11e370e74c1386a39d8192d"
    access_key = "?access_key=" + ACCESS_KEY
    currency = "GBP,USD" # More currency conversion rate can be added; Check: Show
    symbols = "&symbols=" + currency
    url += access_key + symbols # Url form

    ### load and save ###
    response = requests.get(url) # Request: fetch data
    data = response.text # Convert data to string 
    obj = json.loads(data) # Convert data to json data type: python dict type
#    print("Out: ", obj) # Control message
    
    ### Extract API Values ###
    date = obj["date"] # Extract date 
    gbp_rate = obj["rates"]["GBP"] # Read Value for gbp rate
    usd_rate = obj["rates"]["USD"] # Read Value for usd rate
#   print("On " +  date + " 1 EUR equals " + str(gbp_rate)+ " GBP, and " + str(usd_rate)+ " USD.") # Display fetched values
    return (date,gbp_rate, usd_rate)

