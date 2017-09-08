import bs4 as bs
import urllib.request


web="https://scraping-challenge.herokuapp.com/useragent"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}



request=urllib.request.Request(web,headers=hdr)
source = urllib.request.urlopen(request).read()

#También valido
#source = requests.get(web)
#soup = bs.BeautifulSoup(source.content,'lxml')

soup = bs.BeautifulSoup(source,'lxml')

panel_body=soup.find_all('div', class_="person panel panel-default")

for item in panel_body:
	print("-----------------------------------")
	#atributo = item.find_all('div', class_="col-md-4")
	#print(atributo[0].text.replace('\n',' '))
	
#	for atributo in item.find_all('div', class_="col-md-4"):
#		print(atributo.text.replace('\n',' '))
	for atributo in item.find_all('div', class_="col-md-4"):
		valor = atributo.find_all('div')
		print(valor[0].text+": "+valor[1].text)

