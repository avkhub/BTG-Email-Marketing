import json
import urllib
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

gs_json_key = json.load(open('Gspread - BooksThatGrow-9b49ca1e3b57.json'))
gs_scope = ['https://spreadsheets.google.com/feeds']


# def access_gsheets(gs_json_key , gs_scope):
# 	gs_credentials = SignedJwtAssertionCredentials(gs_json_key['client_email'], gs_json_key['private_key'], gs_scope)
# 	gc = gspread.authorize(gs_credentials)
# 	wks = gc.open("Email Extraction").sheet1
# 	val = wks.acell('A1').value	
# 	print val

def access_kimonoapi():
	results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/92mkaxfe?apikey=CeLkREglLULmtAtjf4ah6BUCcSBhGpyd"))
	print results

# access_gsheets(gs_json_key , gs_scope)
access_kimonoapi()





