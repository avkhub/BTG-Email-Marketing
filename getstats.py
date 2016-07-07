import requests
import json

def get_bounced():
    request = requests.get(
        "https://api.mailgun.net/v3/booksthatgrow.org/campaigns/fqyvq/events?event=bounced",
        auth=('api', 'key-2ae31b0f7b54ef7680b835894e2131cc'))

    # print 'Status: {0}'.format(request.status_code)
    # print 'Body: {0}'.format(request.text) 
    unique = []
    results = (json.loads(request.text))
    for item in results:    	
    	if item["domain"] not in unique:
    		unique.append(item["domain"])
    return unique
    print 
# def get_opened():
# 	request = requests.get(
#         "https://api.mailgun.net/v3/booksthatgrow.org/campaigns/fqyvq/events?event=opened",
#         auth=('api', 'key-2ae31b0f7b54ef7680b835894e2131cc'))

# 	unique = [] 
# 	results = (json.loads(request.text))
# 	for item in results:
#     	if item["recipient"] not in unique:
#     		item["count"] = 0
#     		item["count"] = item["count"] + 1
#     		unique.append(str(item["recipient"] + "," + str(item["count"])))
#     	item["count"] = item["count"] + 1
#     return 	results


def get_clicked():
    request = requests.get(
        "https://api.mailgun.net/v3/booksthatgrow.org/campaigns/fqyvq/delivered?groupby=recipient",
        auth=('api', 'key-2ae31b0f7b54ef7680b835894e2131cc'))

    # print 'Status: {0}'.format(request.status_code)
    # print 'Body: {0}'.format(request.text) 
    unique = []
    count = 0     
    results = (json.loads(request.text))
    for item in results:  
    	count = count + 1
    	print count   	
    	print item

    # 	if item["recipient"] not in unique:
    # 		item["count"] = 0
    # 		item["count"] = item["count"] + 1
    # 		unique.append(str(item["recipient"] + "," + str(item["count"])))
    # 	item["count"] = int(item["count"]) + 1	

    # return results


def get_delivered():

	request = requests.get(
        "https://api.mailgun.net/v3/booksthatgrow.org/campaigns/fqyvq/events?event=delivered",
        auth=('api', 'key-2ae31b0f7b54ef7680b835894e2131cc'))

	unique = [] 
	count = 0
	results = (json.loads(request.text))
	for item in results:
		# if item["recipient"] not in unique:
			count = count + 1
			print count
			print item
			# unique.append(item["recipient"])


def get_lists():
	lists = []
	get_lists = requests.get(
		"https://api.mailgun.net/v3/lists",
		auth=('api','key-2ae31b0f7b54ef7680b835894e2131cc'))


	res = (json.loads(get_lists.text))
	for item in res["items"]: 
		lists.append(item["address"])
	return lists

def list_members():
	members = []
	count = 0
	lists = get_lists()
	for item in lists:
		print item
		request = requests.get(
			"https://api.mailgun.net/v3/lists/"+item+"/members",
			auth=('api','key-2ae31b0f7b54ef7680b835894e2131cc'))
    
		results = (json.loads(request.text))
		
		for item in results["items"]:
			members.append(item["address"])
			count = count + 1
			print count
			


def get_bounces(bounces,bounced_url,bounce_count, bounces_visited_urls):
	
	if(bounced_url not in bounces_visited_urls):
    		request = requests.get(bounced_url,auth=('api','key-2ae31b0f7b54ef7680b835894e2131cc'))
    		results = (json.loads(request.text))    	
    		bounces_visited_urls.append(bounced_url)
    		for item in results["items"]:
    			
    			if(item["address"] not in bounces):
    				print item["address"]
    				bounces.append(item["address"])
    				bounce_count = bounce_count + 1
    				print bounce_count
    		if(results["paging"]["next"]) is not None:
    			bounced_url = results["paging"]["next"]
    			get_bounces(bounces , bounced_url , bounce_count , bounces_visited_urls)
    		else:
    			print "No Next URL"

# def get_logs(delivered,delivered_count,delivered_url , delivered_visited_urls):
#     request = requests.get(
#         delivered_url,
#         auth=("api", "key-2ae31b0f7b54ef7680b835894e2131cc"),
#         params={"begin"       : "Tue, 25 August 2015 09:00:00 -0000",
#         		"limit"		  : "5",
#         		"event" 	  : "delivered"})

#     results = (json.loads(request.text))   
#     # print results
#     if((results["paging"]["next"] is not None) and (results["paging"]["next"] not in delivered_visited_urls)):
#     	delivered_url = results["paging"]["next"]
#     	print delivered_url
#     	delivered_visited_urls.append(delivered_url)
#     	get_logs(delivered , delivered_count ,delivered_url ,delivered_visited_urls)

def get_opens(opened,open_page_count,opened_count):
	request = requests.get(
		"https://api.mailgun.net/v3/booksthatgrow.org/campaigns/fqyvq/opens?groupby=recipient&page="+str(open_page_count),
		auth=("api", "key-2ae31b0f7b54ef7680b835894e2131cc"))  
	results = (json.loads(request.text))
	# print results
	count = 0
	for item in results:
		print item
		opened.append(item["recipient"])
		count = count+1
		opened_count = opened_count+1
		print opened_count
	if(count != 0):
		open_page_count = open_page_count + 1
		get_opens(opened , open_page_count , opened_count)





def remove_member():
    return requests.delete(
        ("https://api.mailgun.net/v3/lists/LIST@booksthatgrow.org/members"
         "/bar@example.com"),
        auth=('api', 'key-2ae31b0f7b54ef7680b835894e2131cc'))




bounces = [] 
bounce_count = 0
bounced_url = "https://api.mailgun.net/v3/booksthatgrow.org/bounces"   	
bounces_visited_urls = []
get_bounces(bounces,bounced_url,bounce_count,bounces_visited_urls)

# delivered = []
# delivered_count = 0
# delivered_url = "https://api.mailgun.net/v3/booksthatgrow.org/events"
# delivered_visited_urls = []
# get_logs(delivered,delivered_count,delivered_url,delivered_visited_urls)


opened = []
open_page_count = 1
opened_count = 0
# get_opens(opened,open_page_count,opened_count)



# list_members()
# result_bounced = get_bounced()
# result_clicked = get_clicked()
# print result_clicked

# result_clicked = get_clicked()
# result_opened = get_opened()

