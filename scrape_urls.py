import requests
import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials
import urllib
import re
import time

def access_gsheets(gs_json_key , gs_scope):
	sheet1 = "Master"
	gs_credentials = SignedJwtAssertionCredentials(gs_json_key['client_email'], gs_json_key['private_key'], gs_scope)
	gc = gspread.authorize(gs_credentials)
	wks = gc.open("Email Address Sourcing - Jose").sheet1
	print "done"
	return wks


def scrape(wks):
	email_list = []
	scrapelist = []
	fulllist = wks.get_all_values()
	url_list = wks.col_values(4)
	
	# del url_list[0:674]
	del fulllist[1680:]
	del fulllist[0:1665]
	for item in fulllist:
		print item
		scrapelist.append(item[2]+','+item[3])
	# for item in scrapelist:
	# 	print item
	
	# for item in url_list:		
	# 	# item = item.split(',')
	# 	print item
	# 	page = urllib.urlopen(item)
	# 	content = page.read()
	# 	# print content
	# 	# print re.findall(r"\+\d{2}\s?0?\d{10}",content)
	# 	# print re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",content)
	# 	email_list.append(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",content))
	# return email_list

	for index , item in enumerate(scrapelist):	
			
		item = item.split(',')
		print item[1]
		page = urllib.urlopen(item[1])
		content = page.read()
		# print content
		# print re.findall(r"\+\d{2}\s?0?\d{10}",content)
		# print re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",content)
		email_list.append(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",content))
		if (index != len(scrapelist)-1):
			print scrapelist[index].split(",")[0]
			print scrapelist[index+1].split(',')[0]
			gs_json_key = json.load(open('Gspread - BooksThatGrow-9b49ca1e3b57.json'))
			gs_scope = ['https://spreadsheets.google.com/feeds']
			if(scrapelist[index].split(",")[0] != scrapelist[index+1].split(',')[0]):
				print "success"
				writeinexcel(gs_json_key,gs_scope,email_list,item[0])
				del email_list[0:]
		else:
			writeinexcel(gs_json_key,gs_scope,email_list,item[0])
			del email_list[0:]
			
	# return email_list



# def writeinexcel(emails,gs_json_key,gs_scope):
# 	gs_credentials = SignedJwtAssertionCredentials(gs_json_key['client_email'], gs_json_key['private_key'], gs_scope)
# 	gc = gspread.authorize(gs_credentials)
# 	wks = gc.open("scrapped emails").sheet1
# 	count = 1	
# 	unique = []
# 	for item in emails:
# 		for i in item:		
# 			if(i not in unique):	
# 				try:
# 					unique.append(i)
# 					wks.update_cell(count, 6, i)
# 					count = count + 1
# 					print i
# 					print count
# 				except:
# 					continue


def writeinexcel(gs_json_key,gs_scope,emails,sheetname):
	# print sheetname
	gs_credentials = SignedJwtAssertionCredentials(gs_json_key['client_email'], gs_json_key['private_key'], gs_scope)
	gc = gspread.authorize(gs_credentials)
	excel = gc.open("New Jersey")	
	wkslist = excel.worksheets()
	# wks = excel.worksheet(" Boise")
	sheetlist = []
	for item in wkslist:
		s = str(item)
		substring1 = "<Worksheet '"
		substring2 = "' id"
		my_string = s[(s.index(substring1)+len(substring1)):s.index(substring2)]
		# print my_string
		sheetlist.append(my_string)

	if(sheetname[21:] not in sheetlist):
		print sheetname[21:]
		worksheet = excel.add_worksheet(title = sheetname[21:] , rows = "10000" , cols = "1")
		worksheet = excel.worksheet(sheetname[21:])
	else:
		worksheet = excel.worksheet(sheetname[21:])
		worksheet.add_cols(1)
		print worksheet.col_count
	count = 1	
	unique = []
	for item in emails:
		for i in item:		
			if(i not in unique):	
				try:
					unique.append(i)
					worksheet.update_cell(count, worksheet.col_count, i)
					count = count + 1
					# print i
					# print count
				except:
					continue









gs_json_key = json.load(open('Gspread - BooksThatGrow-9b49ca1e3b57.json'))
gs_scope = ['https://spreadsheets.google.com/feeds']
wks = access_gsheets(gs_json_key,gs_scope)
scrape(wks)
# emails = scrape(wks)
# writeinexcel(emails,gs_json_key,gs_scope)

