# Mike Taatgen
# 01-13-14
# DPW

import webapp2
from library import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):
    	page = Page() # creates an instance of the Page function which is defined at library.py
    	title = "Welcome to the calculator"
		self.response.write(page.head()) # Creates the HTML attributes
		
		mike = Person(5555) # Password for his/her voicemail
		mike.name = "Mike Taatgen" # Name of the user
		mike.text = 45 #Amount of text send
		mike.minutes = 300 # Amount of minutes talked on the phone
		mike.internet =  2 # Amount of GB used for data
		
		anthony = Person(5235) # Password for his/her voicemail
		anthony.name = "Anthony Kluba" # Name of the user
		anthony.text = 25 #Amount of text send
		anthony.minutes = 325 # Amount of minutes talked on the phone
		anthony.internet = 2.2 # Amount of GB used for data

		nate = Person(1821) # Password for his/her voicemail
		nate.name = "Nathan Dickison" # Name of the user
		nate.text = 75 #Amount of text send
		nate.minutes = 290 # Amount of minutes talked on the phone
		nate.internet = 3.2 # Amount of GB used for data

		jairo = Person(8371) # Password for his/her voicemail
		jairo.name = "Jairo Jurado" # Name of the user
		jairo.text = 25 #Amount of text send
		jairo.minutes = 400 # Amount of minutes talked on the phone
		jairo.internet =  1 # Amount of GB used for data
		
		rebecca = Person(9213) # Password for his/her voicemail
		rebecca.name = "Rebecca Carroll" # Name of the user
		rebecca.text = 49 #Amount of text send
		rebecca.minutes = 280 # Amount of minutes talked on the phone
		rebecca.internet = 4 # Amount of GB used for data

		
		players = [mike,anthony,nate,jairo,rebecca]	
		
		#self.response.write(heroes[1].name)
		for h in players:
			self.response.write("<div>" + h.name + " -- "   + "</div>" )
			
			self.response.write(self.html(players[0]))
				
		def html(self,player): 
			total = (player.text * .25) + (player.minutes * 0.04) + (player.internet * 8.5)
			code = '''
			<h1>{player.name}</h1>
			<div>
				<p>
					<h2>Amount of texts</h2>
					<span>{player.text} Texts</span>
				</p>
				<p>
					<h2>Amount of minutes talked</h2>
					<span>{player.minutes} Minutes</span>
				</p>
				<p>
					<h2>Amount of GB used for data</h2>
					<span>{player.internet} GB</span>
				</p
				<p>
					<h2>Monthly fee</h2>
					<span>{total}$</span>
				</p>
			</div>
			'''	
			code = code.format(**locals())
			return code	
		
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

class Person(object):
	def __init__(self,pin):
		self.name = ""
		self.text = 0
		self.minutes = 0
		self.__internet = 0
		self.__password = pin
		
	#GETTER FUNCTION	
	@property 
	def password(self):
		return self.__password	
		
	# SETTER FUNCTION	
	#setters can do more
	@password.setter
	def internet(self,value):
		self.__password = value