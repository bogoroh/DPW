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
		self.__user = 'mtaatgen@live.com'
		self.__pass = "dv8kZ24iGNZwFiHdZrClS_vaNCKTz1rY5jO9GckIj-fgVEqcgpcyLA"
		self.__url = "http://webservices.ns.nl/ns-api-avt?station="
		self.__station = "ut"
		self.__req = urllib2.Request(self.__url + self.__station)
		
		#Creates authentication helper
		password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
		#Binds username and pass to url
		password_manager.add_password(None,self.__url+self.__station,self.__user,self.__pass)
		#Stores user and pass to library's authentication helper
		auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)

		#creates "openeer object for fetching page info"
		self.__opener = urllib2.build_opener(auth_manager)
		urllib2.install_opener(self.__opener)
		#requests and brings back page info
		handler = urllib2.urlopen(self.__req)
		#prints out to the page
		self.response.write(handler.read())

		page = Page()
		form_settings = [{"name":"station","type":"text","label":"Enter the abrevation of the station "},{"name":"submit","type":"submit","label":"Get departure times"}]
		form = Form(form_settings)
		form.update()
		self.response.write(form.header + form.getForm + form.close)
		if self.request.GET:
			self.__station = self.request.GET['station']
			openerURL = urllib2.build_opener() #magic to load request - creates framework to get url
			result = openerURL.open(self.__req) # gets url and puts result in "result"
			#print result
			xmldoc = minidom.parse(result) #parse through string to get XML object 

			content = '<br/>' 
			FList = xmldoc.getElementsByTagName('RitNummer')
			self.response.write(FList[0].firstChild.nodeValue)
			#for l in FList:
				#content += 'Trainnumber: ' + l.attributes["RitNummer"].value 
				#content += 'Departure Time: ' + l.attributes["VertrekTijd"].value
				#content += 'Final Destination: ' + l.attributes["EindBestemming"].value
				#content += 'Traintype: ' + l.attributes["TreinSoort"].value
				#content += 'Departure Railway: '  + l.attributes["VertrekSpoor"].value
				#content += "<br/>"
			#self.response.write(content)
			
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
