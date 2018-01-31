# coding:utf8
from urllib.request import urlopen
import time
 
for n in range(1,42):

	url_webpage = 'http://www.parl.gc.ca/About/Parliament/FederalRidingsHistory/hfer.asp?Language=E&Search=Gres&genElection=' + str(n) +'&ridProvince=0&submit1=Search'
	print(url_webpage)
	file_path = '/Users/etienne/Desktop/TestN/General_Election_' + str(n) + '.html'

	response = urlopen(url_webpage)

	html_file = open(file_path, "wb")

	html_file.write(response.read())

	html_file.close()

	print ("J'ai terminé avec" + file_path + '!')

	time.sleep(1)