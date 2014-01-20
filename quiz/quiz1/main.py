# Mike Taatgen
# 01-15-14
# DPW
# Quiz 1

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
		print calcArea(20,20)
		countDown(20)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

def calcArea (w,h):
	area = str(w * h) #Equation to calculate the area

	if (w == h): #if the width is equal to the height
		areaMessage = "The area of your square is " + area + " square feet."
		return areaMessage
	else: # If the width is not equal to the height
		areaMessage = "The area of your rectangle is " + area + " square feet."
		return areaMessage

def countDown (b):
	bottles = int(b)
	for i in range(bottles, 0, -1): #bottles is the amount of beer bottles on the wall
		if i == 1: # If you're grabbing the last beer
			print "1 Bottle of beer on the wall, 1 Bottle of beer." +  "Bottles of Beer.. take one down and pass it around. Now you are out of beer and kind of drunk !"
			print "BURP, BURP, HICK, HICK"
		else:
			message = str(i) + " Bottles of Beer on the Wall, " + str(i) +  " Bottles of Beer.. take one down and pass it around. Now you have " + str(i-1) + " bottles of beer on the wall!"
			print message
			print "----------------------------------------------"