





import requests
import csv
import xlrd
import os
import requests
import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials
import urllib
import re



def add_list_member():
    gs_json_key = json.load(open('Gspread - BooksThatGrow-9b49ca1e3b57.json'))
    gs_scope = ['https://spreadsheets.google.com/feeds']
    gs_credentials = SignedJwtAssertionCredentials(gs_json_key['client_email'], gs_json_key['private_key'], gs_scope)
    gc = gspread.authorize(gs_credentials)
    wks = gc.open("New Jersey")
    sheet = wks.worksheet(" Great Falls")
    request = requests.post(
        "https://api.mailgun.net/v3/lists",
        auth=('api', 'key-2ae31b0f7b54ef7680b835894e2131cc'),
        data={'address': 'scrapedlist18@booksthatgrow.org',
              'description': "scrapedlist18"})

    members = sheet.col_values(1)
    counter = 1 
    # del members[1:5166]
    for item in members:

        print item              
        request = requests.post(
                "https://api.mailgun.net/v3/lists/scrapedlist18@booksthatgrow.org/members",
                auth=('api', 'key-2ae31b0f7b54ef7680b835894e2131cc'),
                data={'subscribed': True,
                'address': item})
        print counter
        counter = counter + 1
    print "Done"  

add_list_member()  


