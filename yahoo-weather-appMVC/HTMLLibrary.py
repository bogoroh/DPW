class WeatherView(object):
	def __init__(self, FList):
		self.__content = '<br/>' + 	FList.title
		for l in FList.forecast:
			self.__content += l["day"] + ' : '
			self.__content += ' - HIGH: ' + l["high"]
			self.__content += ' - LOW: ' + l["low"]
			self.__content += '<img src="images/'+l['code']+'.png" width="50" height="50" />'
			self.__content += "<br/>"

	@property
	def content(self):
	    return self.__content #Return the code.. So we can print it in main

			

class Page(object):
	def __init__(self):
			self.title = "Main"
			self.css = '<link rel="stylesheet" href="css/main.css" type="text/css" />'
			self._header ='''<!DOCTYPE>
<html>
    <head>
        <title>{self.title}</title>
        {self.css}
    </head>
    <body>
       '''   
			self.__closer = '''
    </body>
</html>'''
			self._content = 'This is my content'
	@property
	def header(self):
		return self._header
	
	@property	
	def close(self):
		return self.__closer

	def update(self):
		self._header = self._header.format(**locals())

class Form(Page):
	# name #Type #labels
	#{"name":"zip","type":"text","label":"Enter your zipcode"}
	def __init__(self,obj):
		super(Form,self).__init__()
		self.method = "GET"
		self.action = ""
		self.__formOpen = '''
<form action="{self.action}" method="{self.method}">'''

		self.__inputs = ''
		for el in obj:
			print el['name']
			self.__inputs += '<input type="' + el['type'] +'" value="' + el['label'] +'" name="' + el['name'] + '"></input>'
		self.__formClose = "</form>"

	@property
	def getForm(self):
	    return self.__formOpen + self.__inputs + self.__formClose
	
	def update(self):
		self._header = self._header.format(**locals())
		self.__formOpen = self.__formOpen.format(**locals())
	