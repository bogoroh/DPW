# Mike Taatgen
# DPW
# 01-22-14
# Application

import webapp2
from HTMLLibrary import *
import urllib2 #Needed for importing from URL's
from xml.dom import minidom #convert XML into an object

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        page = Page()
        form_settings = [{"name":"station","type":"text","label":"Enter the station code"},{"name":"submit","type":"submit","label":"Get departure time"}]
        form = Form(form_settings)
        form.update()
        self.response.write(form.header + form.getForm + form.close)
    	if self.request.GET:
    		zip = self.request.GET['station'] # Takes the zipcode form the url and stores it
    		#print "Do this"
    		url = "http://webservices.ns.nl/ns-api-avt?station=" #url we are going to load the page from 
    		reg = urllib2.Request(url + zip) #concat zip with the url and format as request
    		opener = urllib2.build_opener() #magic to load request - creates framework to get url
    		result = opener.open(reg) # gets url and puts result in "result"
    		#print result
    		xmldoc = minidom.parse(result) #parse through string to get XML object 
    		self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)
    		content = '<br/>' 
    		FList = xmldoc.getElementsByTagName('yweather:forecast')

    		for l in FList:
    			content += l.attributes["day"].value  + ' : '
    			content += ' - HIGH: ' + l.attributes["high"].value
    			content += ' - LOW: ' + l.attributes["low"].value
    			content += '<img src="images/'+l.attributes['code'].value+'.png" width="50" height="50" />'
    			content += "<br/>"
    		self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
