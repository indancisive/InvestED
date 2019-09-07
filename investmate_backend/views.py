from django.shortcuts import render
import sqlite3

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
    ltgURL = f"/results/{sector}/longTermGrowth/"
    # 2. High Potential Return
    hprURL = f"/results/{sector}/highPotentialReturn"
    # 3. Currently Undervalued
    cuURL = f"/results/{sector}/currentlyUndervalued"
    # 4. Well-Roundedness
    wrURL = f"/results/{sector}/wellRoundedness"
    
    urls = {'long': ltgURL, 'high_return':hprURL, 'currently_undervalued':cuURL,'well_rounded': wrURL}
    return render(request, 'guide2.html', urls)

def results(request, sector, dog):
    '''
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.execute("SELECT * FROM investmate_backend_stock")
    rows = cursor.fetchall()
    args = {'test': rows}
    '''
    sector += "dan"
    args = {'test': sector + dog}
    
    return render(request, 'results.html', args)