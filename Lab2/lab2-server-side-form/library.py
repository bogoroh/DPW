class Page():
	def __init__(self):
		self.__header ='''<!DOCTYPE>
<html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" href="css/main.css" type="text/css" />
    </head>
    <body>
       '''   
		self.__closer = '''
    </body>
</html>'''
	
	def open(self):
		return self.__header
		
	def close(self):
		return self.__closer