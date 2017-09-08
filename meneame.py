import bs4 as bs
import urllib.request
import re



web="https://www.meneame.net/?page="
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


for i in range(1,3):
	request=urllib.request.Request(web+str(i),headers=hdr)
	source = urllib.request.urlopen(request).read()
	soup = bs.BeautifulSoup(source,'lxml')

	body= soup.find_all('div', class_='center-content')

	for body in soup.find_all('div', class_='center-content'):
		for noticia in body.find_all('h2'):
			for titulo in noticia.find_all('a'):		
				print (titulo.text + "   -->"+titulo.get('href'))



"""Destacadas y mas votadas"""
request=urllib.request.Request(web+str(1),headers=hdr)
source = urllib.request.urlopen(request).read()
soup = bs.BeautifulSoup(source,'lxml')

destacadas = soup.find_all('div', class_="sidebox red")

for item in destacadas:
	for celdas in item.find_all('div', class_='cell'):
		for contador in celdas.find_all('span'):
			print (contador.text)
