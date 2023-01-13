# Import the required modules
import requests
from bs4 import BeautifulSoup
import json

with open('index.html','r') as ip:
    iptxt = ip.read()
    print(iptxt)
bsp = BeautifulSoup(iptxt,'html.parser')
caps = []
for item in bsp.find_all('li'):
    cp = item.strong.text.strip() # finding the text inside strong tag 
    st = item.span.text.strip()  # finding the text inside span tag
    caps.append({'capital':cp,'state':st}) # creating a dictionary and appending the values 
    # framing the result in dictionary
    result_json = {
        'capitals': caps,
        'summary':{
            'number_of_capitals':len(caps)
        }
    }
#print(result_json)
r = json.dumps(result_json,indent=4)
with open('results.json','w') as res:
    res.write(r)
print(r)









