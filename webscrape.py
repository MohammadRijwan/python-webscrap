import requests
from bs4 import BeautifulSoup

def news():
# the target we want to open
	url='http://www.hindustantimes.com/top-news'

	#open with GET method 
	resp=requests.get(url) 
	print(resp)

#http_respone 200 means OK status 
	if resp.status_code==200: 
		print("Successfully opened the web page") 
		print("The news are as follow :-\n") 

	# we need a parser,Python built-in HTML parser is enough . 
		s=BeautifulSoup(resp.text,'html.parser')
		#print(s)	 

	# l is the list which contains all the text i.e news 
		l=s.find("div")
		#print(l)

	#now we want to print only the text part of the anchor. 
	#find all the elements of a, i.e anchor 
		for i in l.findAll("div",{"class":"media-heading headingfour"}): 
			print("--------------------------------------")
			print(i.find("a")) 
			print("--------------------------------------")
	else: 
		print("Error")

news()

