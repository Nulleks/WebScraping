import requests
from bs4 import BeautifulSoup



##https://www.youtube.com/watch?v=3xQTJi2tqgk

url = "http://www.yellowpages.com/search?search_terms=cofee&geo_location_terms=Los+Angeles%2C+CA"
url_page_2 = url+"&page="+ str(2)

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

g_data = soup.find_all("div", {"class": "info"})


for item in g_data:
	print (item.contents[0].find_all("a", {"class": "business-name"})[0].text)
	print (item.contents[1].find_all("p", {"class": "adr"})[0].text)
	
	try:	
		print (item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text)
	except:
		pass
	try:	
		print (item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text)
	except:
		pass
	try:
		print (item.contents[1].find_all("div", {"class": "phones phone primary"})[0].text)
	except:
		pass


