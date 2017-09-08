import bs4 as bs
import urllib.request
import pandas as pd



web="https://scraping-challenge.herokuapp.com/onepage"
df= pd.DataFrame()

request=urllib.request.Request(web)
source = urllib.request.urlopen(request).read()

#También valido
#source = requests.get(web)
#soup = bs.BeautifulSoup(source.content,'lxml')

soup = bs.BeautifulSoup(source,'lxml')

panel_body=soup.find_all('div', class_="person panel panel-default")

for item in panel_body:
	df2=pd.DataFrame()
	print("-----------------------------------")
	#atributo = item.find_all('div', class_="col-md-4")
	#print(atributo[0].text.replace('\n',' '))
	
#	for atributo in item.find_all('div', class_="col-md-4"):
#		print(atributo.text.replace('\n',' '))
	for atributo in item.find_all('div', class_="col-md-4"):
		valor = atributo.find_all('div')
		df2[valor[0].text.replace('\n','').replace('\r','').replace(' ','_')]=[valor[1].text.replace('\n','').replace('\r','').replace(' ','')]
		#print(valor[0].textvalor[0].text+": "+valor[1].text.replace('\n','').replace('\r','').replace(' ',''))
	print(df2)
	if df.empty:
		df = df2
	else:
		df = df.append(df2)

print(df.shape) #100 Pasajeros 20 columnas
df.to_csv('out.csv')

