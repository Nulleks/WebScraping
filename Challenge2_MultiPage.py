import bs4 as bs
import urllib.request



url='https://scraping-challenge.herokuapp.com/pagination?page='

for i in range(0,50):
	request=urllib.request.Request(url+str(i))
	source = urllib.request.urlopen(request).read()
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
			print(valor[0].text+": "+valor[1].text.replace('\n','').replace('\r','').replace(' ',''))


