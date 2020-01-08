import requests 
from bs4 import BeautifulSoup
from datetime import datetime
import time



# Build by Anilabha Baral



def Amazon_handler(): 
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("Time: ", current_time)
	print("Connecting to amazon...")
	URL = "https://www.amazon.in/Oppo-Aurora-Blue-64GB-Storage/dp/B07PQ7CXLV/"
   
	r = requests.get(URL) 
	soup = BeautifulSoup(r.content, 'html5lib') 
	print("Fetching price...")
	js_test = soup.find('span', id ='priceblock_ourprice') 
	if js_test is None: 
		js_test = soup.find('span', id ='priceblock_dealprice')		 
	str = "" 
	for line in js_test.stripped_strings : 
		str = line 

	# To integer
	str = str[1:]
	str = str.replace(",", "")
	str = str.replace(" ", "")
	current_price = int(float(str)) 
	print("Current price = ", current_price) 
	


while True: 
	Amazon_handler()
	print("Will fetch again after 1 minute. To stop press ctl + c...")
	time.sleep(60) 
