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
		pass

class Wakeboard(Sport):
	def __init__(self):
		super(Wakeboard, self).__init__()

class Snowboard(Sport):
	def __init__(self):
		super(Snowboard, self).__init__()
