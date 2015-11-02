#Base URL: https://foia.state.gov/searchapp/Search/SubmitSimpleQuery
#caseNumber = F-2014-20439

#Answer to 1 
#https://foia.state.gov/Search/results.aspx?searchText=*&caseNumber=F-2014-20439

#Answer to 2
#https://foia.state.gov/Search/results.aspx?searchText=Benghazi&caseNumber=F-2014-20439

#Answer to 3 - I'm using a different request URL because I found more parameters on a repository that scraped Hillary's e-mails.
import urllib2, json 
import re

def clean_json(json):
    '''
    Turn dirty State Department JSON into clean JSON.
    '''
    return re.sub(r'new Date\(.*?\)', '""', json)

dirty_json = urllib2.urlopen('https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?_dc=1446441182320&searchText=benghazi&beginDate=false&endDate=false&collectionMatch=Clinton_Email&postedBeginDate=false&postedEndDate=false&caseNumber=false&page=1&start=0&limit=500').read()
valid_json = clean_json(dirty_json)

data = json.loads(valid_json)

for links in data['Results']:
    print links['pdfLink']

