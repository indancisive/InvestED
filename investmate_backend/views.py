from django.shortcuts import render
import sqlite3

# Create your views here.
def index(request):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.execute("SELECT * FROM investmate_backend_stock")
    rows = cursor.fetchall()
    args = {'test':rows}
    return render(request, 'index.html', args)