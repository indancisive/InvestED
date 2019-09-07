# This module is run to index Global Investment Research into a database to improve website load times
# It takes advantage of multiple Marquee API endpoints to get a complete picture of a stock's fundamental investment contexts

import requests
import json
#Import secret API keys
from secret import marquee_client_id, marquee_client_secret
import sqlite3
con = sqlite3.connect('db.sqlite3')

def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO investmate_backend_stock(name, ticker, sector, description, financialReturnScore, growthScore, multipleScore, integratedScore) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entities)
    con.commit()

# Authentication
auth_data = {
    "grant_type"    : "client_credentials",
    "client_id"     : marquee_client_id,
    "client_secret" : marquee_client_secret,
    "scope"         : "read_product_data"
}

# create session instance
session = requests.Session()

auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data = auth_data)
access_token_dict = json.loads(auth_request.text)
access_token = access_token_dict["access_token"]

# update session headers with access token
session.headers.update({"Authorization":"Bearer "+ access_token})

request_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query"

request_query = {
                    "startDate": "2013-01-15",
                    "endDate":"2018-01-15"
               }

request = session.post(url=request_url, json=request_query)
results = json.loads(request.text)

# Loop that removes duplicate GSIDs (unique, internal stock identifiers)
usedNumbers = []
x = 0
for result in results['data']:
    # Typecast temp_gsid to int for 'in' function checks
    temp_gsid = int(result['gsid'])
    if temp_gsid in usedNumbers:
        continue
    # If not duplicate GSID, checks Marquee USCANFPP dataset and pulls context indicators and ticker from another API endpoint
    else:
        # Prevents duplicate GSIDs
        usedNumbers.append(temp_gsid)
    
        # Pulls investment context data from dataset
        try:
            financialReturnsScore = result['financialReturnsScore']
        except:
            financialReturnsScore = 0
        try:
            growthScore = result['growthScore']
        except:
            growthScore = 0
        try:
            multipleScore = result['multipleScore']
        except:
            multipleScore = 0
        try:
            integratedScore = result['integratedScore']
        except:
            integratedScore = 0
    
        # Construct URL to access /assets GET endpoint using string literal to insert GSID
        request_url = f"https://api.marquee.gs.com/v1/assets?gsid={temp_gsid}"
        request = session.get(url=request_url)
        results = json.loads(request.text)
        # Loops through dataset and extracts stock ticker from queried data
        for temp_dict in results['results'][0]['identifiers']:
            if 'TKR' in temp_dict.values():
                ticker = temp_dict['value']
                continue
        entities = ("name", ticker, "sector", 'IT', financialReturnsScore, growthScore, multipleScore, integratedScore)
        sql_insert(con, entities)
        print('sql write success')
        