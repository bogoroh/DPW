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

		page = Page()
		form_settings = [{"name":"station","type":"text","label":"Enter the abrevation of the station "},{"name":"submit","type":"submit","label":"Get departure times"}]
		form = Form(form_settings)
		form.update()
		self.response.write(form.header + form.getForm + form.close)
		if self.request.GET:
			print "I ran"
			self.response.write(self.request.GET['station']) 
			self.__station = self.request.GET['station']
			self.__user = 'mtaatgen@live.com' #Authenticator username
			self.__pass = "dv8kZ24iGNZwFiHdZrClS_vaNCKTz1rY5jO9GckIj-fgVEqcgpcyLA"

			self.__url = "http://webservices.ns.nl/ns-api-avt?station=" #URL from the API
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
			handler = urllib2.urlopen(self.__req)
			openerURL = urllib2.build_opener() #magic to load request - creates framework to get url
			result = openerURL.open(self.__req) # gets url and puts result in "result"
			xmldoc = minidom.parse(result) #parse through string to get XML object 
			content = '<br/>' 
			ARit = xmldoc.getElementsByTagName('RitNummer')
			AVertrekTijd = xmldoc.getElementsByTagName('VertrekTijd') # Saved the departure time for that station into an array
			AEind = xmldoc.getElementsByTagName('EindBestemming') # Saves all the final destination into an array  for that station
			ATrein = xmldoc.getElementsByTagName('TreinSoort') # Saves all the Traintypes in an array for that station
			AVertrek = xmldoc.getElementsByTagName('VertrekSpoor') #Saves all the Departure railways for that station into an array 
			self.response.write(AVertrek)
			for l,m,n,o,p in zip(ARit, AVertrekTijd,AEind,ATrein,AVertrek): # Makes it possible to loop throught multiple arrays
				content += 'Trainnumber: ' + l.firstChild.nodeValue 
				content += 'Departure Time: ' + m.firstChild.nodeValue
				content += 'Final Destination: ' + n.firstChild.nodeValue
				content += 'Traintype: ' + o.firstChild.nodeValue
				content += 'Departure Railway: '  + p.firstChild.nodeValue
				content += "<br/>"
			self.response.write(content)
			
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
