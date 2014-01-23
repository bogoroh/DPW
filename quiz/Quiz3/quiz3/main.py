# Mike Taatgen
# Quiz 3
# 01-22-14
# DPW
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

class Sport(object):
	def __init__(self):
		self.__age = 0
		self.__inventory = ''
		self._location = ''

		@property
		def age(self):
		    return self.__age

		@property
		def inventory(self):
		    return self.__inventory    
		
		def Surface(self):
			pass
		def PrintClassName(self):
			print "We're now inside the Abstract Class called: 'Sport' "


class Wakeboard(Sport):
	def __init__(self):
		super(Wakeboard, self).__init__()
		self.__age = 1840
		self.__inventory = 'Wakerope, Wakeboard, Boat'
		self._location = 'Willemstad, Curacao'
		
		@property
		def age(self):
		    return self.__age
		    		
		@property
		def inventory(self):
		    return self.__inventory   
	

		def Surface(self):
			print "This sport is played on the water"
		def PrintClassName(self):
			print "We're now inside the super class called: 'Wakeboard' "

class Snowboard(Sport):
	def __init__(self):
		super(Snowboard, self).__init__()
		self.__age = 1960
		self.__inventory = 'Snowboard, Snowboots, Snow , Mountain'
		self._location = 'Vancoucer, BC'

		@property
		def age(self):
		    return self.__age

		@property
		def inventory(self):
		    return self.__inventory   

		def Surface(self):
			print "This sport is played on snow"
		def PrintClassName(self):
			print "We're now inside the super Class called: 'Snowboard' "