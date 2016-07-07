import requests
import csv
import xlrd
import os

def getdata_excel():
    emaillist = []
    temp = ["Wisconsin Principals.xls"]
    unique_domain = []
    unique_list = []
    fullrow = [] 
    dummy = []
  #   for item in os.listdir(os.getcwd()+"/Daniel/K-12 Principals Database/"):
		# temp.append(item)
    count = 0
    counter = 0
    loopcounter = 0
    for item in  temp:
        workbook = xlrd.open_workbook(os.getcwd()+"/Daniel/K-12 Principals Database/"+item)
        worksheet = workbook.sheet_by_index(0)
        if worksheet.cell(0, 0).value == xlrd.empty_cell.value:
            print "Empty check?? "
        else:
            for i in range(worksheet.nrows):
                fullrow.append(worksheet.row(i))  
            
            unique_list = [[] for i in ((range(worksheet.nrows/200+2)))]
            print unique_list[0]
            print unique_list[1]
            print unique_list[2]
            should_restart=  True
           

            while((should_restart) ):
                should_restart = False
            
                for item in list(fullrow):                    
                        email = str(item[4].value).replace(" ","").replace("\r", " ").replace("\n", " ").replace("\t", '').replace("\"", "")
                        if ("@" in str(email) and (loopcounter<(len(range(worksheet.nrows/200+1))))):
                            splitter = str(email).strip().split("@")
                            # 3 per domain
                            if((unique_domain.count(splitter[1])<5) and (email not in dummy) and (count < 200)):
                                unique_domain.append(splitter[1])
                                dummy.append(email)
                                unique_list[counter].append(item)
                                count = count+1
                                # print count
                                # print item                 
                            elif (count >= 200):
                                del unique_domain[:]
                                # print unique_domain
                                counter = counter+1
                                count = 0
                                # unique_domain.append(splitter[1])
                                # unique_list[counter].append(item)
                                should_restart = True
                                loopcounter = loopcounter+1
                                
                                break
                else:
                        
                        break
            for item in list(fullrow):                
                email = str(item[4].value).replace(" ","").replace("\r", " ").replace("\n", " ").replace("\t", '').replace("\"", "")               
                if (("@" in str(email) )and (email not in dummy)):
                        unique_list[3].append(item)                   
                        
    print len(unique_list[0])
    print len(unique_list[1])
    print len(unique_list[2])
    print len(unique_list[3])
    
    create_mailing_list(unique_list)
    	   # print worksheet.col(0)
        #    FirstName = worksheet.col(0)
        #    LastName = worksheet.col()
        #    Email = worksheet.col()
        #    School = worksheet.col()

def create_mailing_list(unique_list):
    count =1
    for item in unique_list:

    	request = requests.post(
        "https://api.mailgun.net/v3/lists",
        auth=('api', 'key-2ae31b0f7b54ef7680b835894e2131cc'),
        data={'address': 'Wisconsin_PS_'+str(count)+'@booksthatgrow.org',
              'description': "Wisconsin_PS_"+str(count)})
        count = count +1
    	print 'Status: {0}'.format(request.status_code)
    	print 'Body:   {0}'.format(request.text)
    add_list_member(unique_list)

		
def add_list_member(members):
    count  = 1
    for item in members:
        counter = 1
        for i in item:            
            request = requests.post(
                "https://api.mailgun.net/v3/lists/Wisconsin_PS_"+str(count)+"@booksthatgrow.org/members",
                auth=('api', 'key-2ae31b0f7b54ef7680b835894e2131cc'),
                data={'subscribed': True,
                'address': i[4].value,
                'name': i[1].value,
                'last name': i[3].value,
                'description': i[0].value,
                'vars': '{"age": 26}'})
            print counter
            counter = counter + 1
        count = count + 1
        print count

    print "Done"    

getdata_excel()
# create_mailing_list()