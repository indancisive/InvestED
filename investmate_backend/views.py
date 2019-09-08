from django.shortcuts import render
import sqlite3
import json
import requests
from secret import iex_api_token

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def guide(request):
    return render(request, 'guide.html', {})

def guide2(request, sector):
    # Create 4 dynamic urls:
    # 1. Long-Term Growth
    ltgURL = f"/results/{sector}/growthScore/"
    # 2. High Potential Return
    hprURL = f"/results/{sector}/financialReturnScore"
    # 3. Currently Undervalued
    cuURL = f"/results/{sector}/multipleScore"
    # 4. Well-Roundedness
    wrURL = f"/results/{sector}/integratedScore"
    
    urls = {'long': ltgURL, 'high_return': hprURL, 'currently_undervalued':cuURL,'well_rounded': wrURL}
    return render(request, 'guide2.html', urls)

def results(request, sector_type, portfolio_type):
    # Connect to and instantiate SQL database object
    conn = sqlite3.connect("db.sqlite3")
    if sector_type == "All":
        # SQL code that instantiates on SQL object by filtering for specified sector's stocks
        # and sorted descending for the specified investment style's corresponding score
        cursor = conn.execute(f"SELECT * FROM investmate_backend_stock ORDER BY {portfolio_type} DESC")
        rows = cursor.fetchall()
    else:
        # SQL code that instantiates on SQL object by filtering for specified sector's stocks
        # and sorted descending for the specified investment style's corresponding score
        cursor = conn.execute(f"SELECT * FROM investmate_backend_stock WHERE sector = '{sector_type}' ORDER BY {portfolio_type} DESC")
        rows = cursor.fetchall()

        # Query IEX Cloud API for latest stock price
        session = requests.Session()
        top3_stocks_price_list = []
        for x in range(3):
            # Construct URL
            temp_ticker = rows[x][2]
            request_url = f"https://cloud.iexapis.com/stable/stock/{temp_ticker}/quote?token={iex_api_token}"
            response = session.get(url=request_url)
            results = json.loads(response.text)
            top3_stocks_price_list.append(float(results["latestPrice"]))

    args = {'top3_stocks': rows[:3], 'top3_stocks_price_list': top3_stocks_price_list}
    return render(request, 'results.html', args)