# Mike Taatgen
# 01-15-14
# DPW
# Animals

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

class AbstractAnimals(object):
	def __init__(self):
		pass

# Black dolphins class that gets all the attributes from the AbstractAnimals class
class BlackDolphins(AbstractAnimals):
	def __init__(self):
		super(BlackDolphins,self).__init__() #calling AbstractAnimals's init function
		self.Phylum = "Chordata"
		self.Class = "Mammalia"
		self.Order = "Cetacea"
		self.Family = "Delphinidae"
		self.Genus = "Cephalorhynchus"
		self.Url = ""
		self.Alifespan = "Up to 20 years"
		self.Habitat = "On Chile's convoluted coastline, Chilean dolphins prefer to live near areas of particularly strong tidal flow above a steep dropping shelf. They are most commonly found in channels and open coasts and bays. They are also found in areas of tide rips at the mouth of fjords. They prefer cold, shallow water at depths of 3 to 15 m. They may also enter rivers and estuaries and can be seen as far as 5 kilometers upstream."
		self.Geolocation = "Chilean dolphins live in the coastal waters of Chile, ranging from near Valparaiso (33°S) to south of Navarino Island (55°15'S) and as far south as Tierra del Fuego."


# LeopardShark class that gets all the attributes from the AbstractAnimals class
class LeopardShark(AbstractAnimals):
	def __init__(self):
		super(BlackDolphins,self).__init__() #calling AbstractAnimals's init function
		self.Phylum = "Chordata"
		self.Class = "Chondrichthyes"
		self.Order = "Carcharhiniformes"
		self.Family = "Carcharhinidae"
		self.Genus = "Cephalorhynchus"
		self.Url = ""
		self.Alifespan = "Up to 20 years"
		self.Habitat = "On Chile's convoluted coastline, Chilean dolphins prefer to live near areas of particularly strong tidal flow above a steep dropping shelf. They are most commonly found in channels and open coasts and bays. They are also found in areas of tide rips at the mouth of fjords. They prefer cold, shallow water at depths of 3 to 15 m. They may also enter rivers and estuaries and can be seen as far as 5 kilometers upstream."
		self.Geolocation = "Chilean dolphins live in the coastal waters of Chile, ranging from near Valparaiso (33°S) to south of Navarino Island (55°15'S) and as far south as Tierra del Fuego."		