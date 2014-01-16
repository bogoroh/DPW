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
		self.Genus = "Galeocerdo"
		self.Url = ""
		self.Alifespan = "The average lifespan of tiger sharks in the wild is 27 years, though some may live to 50 years of age. "
		self.Habitat = "Tiger sharks are a saltwater species. Although they prefer the sea grass ecosystems of the costal areas, they occasionally inhabit other areas due to prey availability. Tiger sharks spend approximately 36 % of their time in shallow coastlne habitats (Heithaus et al., 2002), generally at depths of 2.5 to 145 m. This species, however, has been documented several kilometers from the shallow areas and at depths up to 350 m. Females are observed in shallow areas more often than males. Tiger sharks have also been documented in river estuaries and harbors"
		self.Geolocation = "Tiger sharks are found in many subtropical and tropical waters, primarily from 45°N to 32°S. Tiger sharks have been sighted from the eastern coast of North America to the eastern coast of Brazil. This includes the coasts of southern North America, Mexico, and Latin America along the Gulf of Mexico. Tiger sharks also populate the coasts of China, India, Africa, Japan, and many islands of the Pacific Ocean."		