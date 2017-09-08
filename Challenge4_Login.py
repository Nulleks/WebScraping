import bs4 as bs
import urllib.request
import mechanicalsoup
import re
from robobrowser import RoboBrowser


#import mechanize
from http.cookiejar import CookieJar


web="https://scraping-challenge.herokuapp.com/login/form"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# Browse to Genius
browser = RoboBrowser(history=True, parser='lxml')
browser.open(web)

# Search for Porcupine Tree
form = browser.get_form(action='/login/auth')

form['email'].value = 'john@doe.com'
form['password'].value = 'johnjohn'
browser.submit_form(form)

soup=browser.parsed

panel_body=soup.find_all('div', class_="person panel panel-default")

for item in panel_body:
	print("-----------------------------------")
	for atributo in item.find_all('div', class_="col-md-4"):
		valor = atributo.find_all('div')
		print(valor[0].text.replace('\n','').replace('\r','').replace(' ','_')+": "+valor[1].text.replace('\n','').replace('\r','').replace(' ',''))
