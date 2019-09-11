# -*- coding: utf-8 -*-

from library import json, requests

def extrator(day, year= '2018', month='09'):
    url = "http://data.fixer.io/api/" + year + "-" + month + "-" + day # only variable day
    ACCESS_KEY = "8d7c453865a1eace07719aa701cc3c36"
    access_key = "?access_key=" + ACCESS_KEY
    waehrungen = "GBP,USD" # more currency conversion rate can be added; Check: Show
    symbols = "&symbols=" + waehrungen
    url += access_key + symbols # Url form

    ### load and save ###
    response = requests.get(url) # Request: Fetch data
    data = response.text # Convert data to string 
    obj = json.loads(data) # Convert data to json data type: python dict type; parsed
#    print("Ausgabe: ", obj) # Controll message
    
    ### Extract API Values ###
    date = obj["date"] # Extract date 
    gbp_rate = obj["rates"]["GBP"] # Read Value for gbp rate
    usd_rate = obj["rates"]["USD"] # Read Value for usd rate
#   print("On " +  date + " 1 EUR equals " + str(gbp_rate)+ " GBP, and " + str(usd_rate)+ " USD.") # Display fetched values
    return (date,gbp_rate, usd_rate)

