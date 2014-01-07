name = input("What is your name? Remember to type in Quotes")
str(name)

day = input("What day is it? Remember to type in Quotes")
str(day)

sunny = input("Is it sunny? (Yes/No) Remember to type in Quotes")
str(sunny)

#If statement for the opening sentence to check if it's sunny or not
if sunny == "Yes":
    opening = "It's a sunny"
else:
    opening = "It's a grimy"
    
print opening

'''{opening} {day}. The ducks were swimmming and it looked like a nomal day at work for {name}.  ''' 
