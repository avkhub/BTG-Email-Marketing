import requests
import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials


def access_gsheets(gs_json_key , gs_scope):
	gs_credentials = SignedJwtAssertionCredentials(gs_json_key['client_email'], gs_json_key['private_key'], gs_scope)
	gc = gspread.authorize(gs_credentials)
	wks = gc.open("FirstSheet").sheet1
	return wks
	

def mailgun(wks):
	mg_key = 'key-2ae31b0f7b54ef7680b835894e2131cc'
	mg_sandbox = 'booksthatgrow.org'
	# mg_recipient = ['adityavarma.k369@gmail.com','aditya@booksthatgrow.com','avk287@nyu.edu']
	# firstname_list = wks.col_values(1)
	# lastname_list = wks.col_values(2)
	email_list = wks.col_values(1)



	request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(mg_sandbox)
	count = 0
	for item in email_list:
		
		print count

		request = requests.post(request_url, auth=('api', mg_key), data={
     		'from': 'Alexa@booksthatgrow.org',
     		'to': 'scrapedlist17@booksthatgrow.org',
    		'subject': 'Books That Grow' ,
    		'o:campaign': 'fqyvq',
     		'html': '''<html>
       			 Ready for the new school year? <br><br>
        		 If you're teaching middle schoolers that struggle with reading, consider <a href="www.booksthatgrow.com/?utm_source=google&utm_medium=email&utm_campaign=BTG_ECAMPAIGN">Books That Grow</a>, a digital book   <br>
        		 collection where every single book is available at multiple complexity levels. <br><br>

        		 With Books That Grow, you can assign one book and challenge every student at their individual reading level, <br>
        		 which is great if you have SPED and ESL students in your class. (Imagine being able to instantly adjust the <br>
        		 reading difficulty of the Declaration of Independence or Edgar Allen Poe's Tell Tale Heart)  Our library is <br>
				 Common Core-aligned and includes fiction, non fiction, and primary source documents. <br><br>
				 We'd love to be apart of your classroom next year. Please visit <a href="www.booksthatgrow.com/?utm_source=google&utm_medium=email&utm_campaign=BTG_ECAMPAIGN">www.BooksThatGrow.com</a> to learn more and if <br>
				 you have question, feel free to email me. <br><br>

        		 Regards,<br><br>
       			 -- 
				 Alexa Golden<br>
				 Teacher Success Lead, Books That Grow<br>
				 Winner, 2014 Verizon Powerful Answers Award<br>
				 <a href="www.booksthatgrow.com/?utm_source=google&utm_medium=email&utm_campaign=BTG_ECAMPAIGN">www.BooksThatGrow.com</a>


                 </html>'''
    	# 	'html': '''<html>
     #   			 Dear Principal %recipient_lname%, <br><br>
     #    		 Could you refer me your Literacy Coordinator please?  <br><br>
     #    		 I'd like to introduce them to <a href="www.booksthatgrow.com/?utm_source=google&utm_medium=email&utm_campaign=BTG_ECAMPAIGN">Books That Grow</a>, an award winning digital reading platform featuring books <br>
     #    		 that increase or decrease in language complexity, based on the reader's ability.  Books That Grow <br>
     #    		 makes it easy for teachers to differentiate instruction and engage struggling readers.  Students can read <br>
     #    		 - at their own level - on laptops, tablets, or even their mobile phones. <br><br>
     #    		 I hope to set up a demo with your Literacy Coordinator and show him/her how Books That Grow can <br>
     #    		 help them improve reading scores.  If you have any questions, feel free to email me at <br>
     #    		 Alexa@BooksThatGrow.org<br><br>
     #    		  Regards,<br><br>
     #   			 -- 
				 # Alexa Golden<br>
				 # Teacher Success Lead, Books That Grow<br>
				 # Winner, 2014 Verizon Powerful Answers Award<br>
				 # <a href="www.booksthatgrow.com/?utm_source=google&utm_medium=email&utm_campaign=BTG_ECAMPAIGN">www.BooksThatGrow.com</a>


     #             </html>'''

     # 		'html': '''<html>
     #   			 Hey there, <br><br>
     #    		 I'm writing to tell you about <a href="http://booksthatgrow.com">Books That Grow</a>, an award winning digital reading platform featuring books <br> that increase or decrease in language complexity, based on the reader's ability.  Books That Grow <br> makes it easy for teachers to differentiate instruction and engage struggling readers.  Our library includes fiction <br> and nonfiction and is appropriate for ELA, Social Studies, and STEM courses.  
     #    		 <br> <br>
				 # As you're planning your curriculum  for the upcoming school year, please keep <a href="http://booksthatgrow.com">Books That Grow</a> in mind. If you have <br> any questions, feel free to email me at Alexa@BooksThatGrow.org
     #   			 <br>
     #   			 <br>
     #   			 Regards,<br><br>
     #   			 -- 
				 # Alexa Golden<br>
				 # Teacher Success Lead, Books That Grow<br>
				 # Winner, 2014 Verizon Powerful Answers Award<br>
				 # <a href="http://booksthatgrow.com">www.BooksThatGrow.com</a>
     #             </html>'''
		})
		
		
		print 'Status: {0}'.format(request.status_code)
		print 'Body:   {0}'.format(request.text) 
		count = count +1



	# firstname_list = wks.col_values(3)
	# lastname_list = wks.col_values(4)
	# email_list = wks.col_values(7)
	# print email_list[3]

	## Do not enable this code - this will send bulk emails *********
	# request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(mg_sandbox)
	# for item in email_list:
	# 	request = requests.post(request_url, auth=('api', mg_key), data={
 #    	'from': 'Alexa@booksthatgrow.org',
 #    	'to': item,
 #    	'subject': 'Hello' + str(firstname_list[0]),
 #    	'text': 'Hello from Mailgun'
	# 	})

	# 	print 'Status: {0}'.format(request.status_code)
	# 	print 'Body:   {0}'.format(request.text) 



gs_json_key = json.load(open('Gspread - BooksThatGrow-9b49ca1e3b57.json'))
gs_scope = ['https://spreadsheets.google.com/feeds']
wks = access_gsheets(gs_json_key , gs_scope)
mailgun(wks)




