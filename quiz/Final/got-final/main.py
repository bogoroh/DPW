# MIke Taatgen
# DPW
# Final
# Game of Thrones

import webapp2
import urllib2
from xml.dom import minidom



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        file = open("GameOfThrones.xml",'r') # To read the local file
        xml = minidom.parseString(file.read()) #to convert the file into an xml object
        #dom = xml.minidom.parse("GameOfThrones.xml")
        topic = xml.getElementsByTagName("name")
        content = " </br>"
        for l in topic:
        	content += l.firstChild.nodeValue
       	self.response.write(content)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
