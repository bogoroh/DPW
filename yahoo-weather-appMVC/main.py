# Mike  Taatgen
# DPW
# 01-20-14
# Yahoo Weather

import webapp2
from HTMLLibrary import *
import urllib2 #Needed for importing from URL's
from xml.dom import minidom #convert XML into an object

class MainHandler(webapp2.RequestHandler):
    ''' This is the main controller for the weather application '''
    def get(self):
    	page = Page()
        #array with dictionary in it
        form_settings = [{"name":"zip","type":"text","label":"Enter your zipcode"},{"name":"submit","type":"submit","label":"Get weather"}]
        form = Form(form_settings)
        form.update()

        self.response.write(form.header + form.getForm + form.close)
    	if self.request.GET:
            wModel = WeatherModel(self.request.GET['zip'])
            wView = WeatherView(wModel.do()) #Instantiates our weather view
            self.response.write(wView.content)
            #self.response.write(content)
        self.response.write(form.close) #closes of the html

class WeatherModel(object):
    ''' This class handles communication with yahoo Weather API, Sends zip, get's weather info in XML, processes the xml and sends data out'''
    def __init__(self,zip):
        self.__url = "http://xml.weather.yahoo.com/forecastrss?p=" #url we are going to load the page from 
        self.__reg = urllib2.Request(self.__url + zip) #concat zip with the url and format as request
        self.__opener = urllib2.build_opener() #magic to load request - creates framework to get url
        self.send() 

    # Send Data    
    def send(self):
        self.__result = self.__opener.open(self.__reg) # gets url and puts result in "result"    
        self.sort()

    # Receive the DATA

    # Sort the data
    def sort(self):
        self.__xmldoc = minidom.parse(self.__result) #parse through string to get XML object 
        self.__do = WeatherData()
        self.__do.title = self.__xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue
        FList = self.__xmldoc.getElementsByTagName('yweather:forecast')
        for l in FList:
            d = l.attributes["day"].value
            h = l.attributes["high"].value
            lw = l.attributes["low"].value
            c = l.attributes["code"].value
            tempDict = dict() # creates a set of info
            tempDict['day'] = d
            tempDict['high'] = h
            tempDict['low'] = lw
            tempDict['code'] = c
            self.__do.forecast.append(tempDict) # Pushes info into the array

    # Return data
    def do(self):
        return self.__do #returns all the info
        #title
        # Forecast - day, high, low , code

class WeatherData(object):
    def __init__(self):
        self.title = '' #Public
        self.forecast = [] # Array 

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
