from django.shortcuts import render
from django.http import HttpResponse
import csv
import os

workpath = os.path.dirname(os.path.abspath(__file__))

# Create your views here.
def home(request):
    
    #Opening the csv file
    c = open(os.path.join(workpath, 'username.csv'), 'r')
    reader = csv.reader(c)
    rows = []
    rownum = 0
    for row in reader:
        # Skip header
        if rownum != 0:
            rows.append(row)
        rownum += 1
    c.close()

    return render(request, 'index.html', {'rows':rows})