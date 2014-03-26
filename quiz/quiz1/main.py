# Mike Taatgen
# 01-15-14
# DPW
# Quiz 1
print calcArea(40,20)

def calcArea (w,h):
	area = str(w * h) #Stringify the area

	if (w == h): #check if the are identical
		area_message = "The area of your square is " + area + " square feet."
		return area_message
	else: # If they are not identical
		areaMessage = "The area of your rectangle is " + area + " square feet."
		return area_message

def countDown (b):
