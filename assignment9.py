# find all the ip address form the given page

import re
import requests

data= requests.get("http://www.guru99.com/ip-address-classes.html").text

p= "(((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))"

for each in re.findall(p,data):
	print(each)