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


# Black dolphins class that gets all the attributes from the AbstractAnimals class
class BlackDolphins(AbstractAnimals):
	def __init__(self):
		super(BlackDolphins,self).__init__() #calling AbstractAnimals's init function
		self.Phylum = "Chordata"
		self.Class = "Mammalia"
		self.Order = "Cetacea"
		self.Family = "Delphinidae"
		self.Genus = "Cephalorhynchus"
		self.Url = "http://www.hdwpapers.com/walls/black_dolphin_wallpaper_2-normal5.4.jpg"
		self.Alifespan = "Up to 20 years"
		self.Habitat = "On Chile's convoluted coastline, Chilean dolphins prefer to live near areas of particularly strong tidal flow above a steep dropping shelf. They are most commonly found in channels and open coasts and bays. They are also found in areas of tide rips at the mouth of fjords. They prefer cold, shallow water at depths of 3 to 15 m. They may also enter rivers and estuaries and can be seen as far as 5 kilometers upstream."
		self.Geolocation = "Chilean dolphins live in the coastal waters of Chile, ranging from near Valparaiso (33°S) to south of Navarino Island (55°15'S) and as far south as Tierra del Fuego."
		self.Sound = "Wieuw Wieuw"


# LeopardShark class that gets all the attributes from the AbstractAnimals class
class LeopardShark(AbstractAnimals):
	def __init__(self):
		super(LeopardShark,self).__init__() #calling AbstractAnimals's init function
		self.Phylum = "Chordata"
		self.Class = "Chondrichthyes"
		self.Order = "Carcharhiniformes"
		self.Family = "Carcharhinidae"
		self.Genus = "Galeocerdo"
		self.Url = "http://www.elasmodiver.com/Sharkive%20images/Leopard_Shark224.jpg"
		self.Alifespan = "The average lifespan of tiger sharks in the wild is 27 years, though some may live to 50 years of age. "
		self.Habitat = "Tiger sharks are a saltwater species. Although they prefer the sea grass ecosystems of the costal areas, they occasionally inhabit other areas due to prey availability. Tiger sharks spend approximately 36&#37; of their time in shallow coastlne habitats (Heithaus et al., 2002), generally at depths of 2.5 to 145 m. This species, however, has been documented several kilometers from the shallow areas and at depths up to 350 m. Females are observed in shallow areas more often than males. Tiger sharks have also been documented in river estuaries and harbors"
		self.Geolocation = "Tiger sharks are found in many subtropical and tropical waters, primarily from 45°N to 32°S. Tiger sharks have been sighted from the eastern coast of North America to the eastern coast of Brazil. This includes the coasts of southern North America, Mexico, and Latin America along the Gulf of Mexico. Tiger sharks also populate the coasts of China, India, Africa, Japan, and many islands of the Pacific Ocean."
		self.Sound = "Wrah Wrah"

# Blue Marlin class that gets all the attributes from the AbstractAnimals class
class BlueMarlin(AbstractAnimals):
	def __init__(self):
		super(BlackDolphins,self).__init__() #calling AbstractAnimals's init function
		self.Phylum = "Chordata"
		self.Class = "Actinopterygii"
		self.Order = "Perciformes"
		self.Family = "Istiophoridae"
		self.Genus = "Makaira"
		self.Url = "http://animaldiversity.ummz.umich.edu/collections/contributors/Grzimek_fish/Scombroidei/Makaira_nigricans/button.jpg"
		self.Alifespan = "The maximum lifespan of females is estimated to be at least 27 years, while males are estimated to live a maximum of 18 years."
		self.Habitat = "Makaira nigricans is an epipelagic and oceanic species. It is the most oceanic of all istiophorids, usually remaining far from land except where the continental shelf is narrow. It can be found in waters with surface temperatures of 22-31C, but it prefers the warm mixed layer above the thermocline, and spends the majority of its time in the uniformly warm near-surface waters from 25-27C. It shows preference for blue waters, at least in the northern Gulf of Mexico."
		self.Geolocation = "<p>Makaira nigricans is distributed mainly in the tropical and temperate waters of the Atlantic, Pacific, and Indian Oceans. It is the most tropical of all billfishes.</p> <p>In the Atlantic Ocean, its range extends to around 40-45N in the North Atlantic and to 40S in the western Atlantic, 30S in the central South Atlantic and 35S in the eastern south Atlantic, but is absent from the Mediterranean Sea. In the Pacific, its range extends to about 45N in the western North Pacific, 35N in the eastern North Pacific, 35S in the western South Pacific, and 25S in the eastern South Pacific. </p> <p> In the Indian Ocean, its range extends to 45S in the southwestern Indian Ocean and 35S in the southeastern Indian Ocean. Larvae are found extensively in the tropical and subtropical waters of the western and central Pacific Ocean, south of Maldives Islands, around the Mascalene Islands, and off the south coasts of Java and Sumatra in the Indian Ocean. In the western central Atlantic, larvae are found off Georgia, North Carolina, Florida, Jamaica, Bahamas, Arecibo, and also off Brazil in the southwest Atlantic. </p>"	
		self.Sound = "Whish Whish"
		
#Array with all the animals in it
animals = [BlackDolphins,LeopardShark,BlueMarlin]

        
class Sound(AbstractAnimals):
    def __init__(self):
        super(Sound, self).__init__()
        
        self.__soundText = '''
        <h2 >The {self.name} says {self.sound}</h2>
    '''
        
    @property
    def soundPass(self):
        return self.__soundText
        
    def update(self):
        self.__soundText = self.__soundText.format(**locals())
        
		
class AbstractAnimals(object):
    def __init__(self):
        self.name = ''
        self.Phylum = ''
        self.Class = ''
        self.Order = ''
        self.Family = ''
        self.Genus = ''
        self.Url = ''
        self.Alifespan = ''
        self.Habitat = ''
        self.Geolocation = ''
        self.Sound = ''
        
