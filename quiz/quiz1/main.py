# Mike Taatgen
# 01-15-14
# DPW
# Quiz 1

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
		self.response.write('Hello world!')
		print calcArea(20,20)
		countDown(20)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

def calcArea (w,h):
	area = str(w * h)

	if (w == h):
		areaMessage = "The area of your square is " + area + " square feet."
		return areaMessage
	else:
		areaMessage = "The area of your rectangle is " + area + " square feet."
		return areaMessage

def countDown (b):
	bottles = int(b)
	for i in range(bottles, 0, -1):
		if i == 1:
			print "1 Bottle of beer on the wall, 1 Bottle of beer." +  "Bottles of Beer.. take one down and pass it around. Now you are out of beer and kind of drunk !"
			print "BURP, BURP, HICK, HICK"
		else:
			message = str(i) + " Bottles of Beer on the Wall, " + str(i) +  " Bottles of Beer.. take one down and pass it around. Now you have " + str(i-1) + " bottles of beer on the wall!"
			print message
			print "----------------------------------------------"
