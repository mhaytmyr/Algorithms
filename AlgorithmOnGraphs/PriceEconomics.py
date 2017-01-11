import json, sys
from urllib.request import urlopen
from time import sleep
def GetData(url):
	data = urlopen(url).read()
	result = json.loads(data.decode("utf-8"))
	print(result.keys())

while True:
	#https://priceonomics.com/jobs/puzzle/
	web = "http://fx.priceonomics.com/v1/rates/"
	GetData(web)
	sleep(1) #sleep one second
