# Mike Taatgen
# DPW
# Final
# Game of Thrones

import webapp2
import urllib2
from xml.dom import minidom



class MainHandler(webapp2.RequestHandler):
    def get(self):
        file = open("GameOfThrones.xml",'r') # To read the local file
        xml = minidom.parseString(file.read()) #to convert the file into an xml object
        FList = xml.getElementsByTagName("name")
        content = ""
        for l in FList:
        	content += l.firstChild.nodeValue
        	content += "</br>"
       	self.response.write(content)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
