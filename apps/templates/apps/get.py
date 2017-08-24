import urllib
import urllib2
def getPage(url):
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	return response.read()
	result = getPage(url)
	f=open('get.html','w')
	f.write(result)
	f.close()
