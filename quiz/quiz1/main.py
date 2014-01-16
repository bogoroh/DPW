# Mike Taatgen
# 01-15-14
# DPW
# Quiz 1

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
		self.response.write('Hello world!')
		print calcArea(20,20)

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

		