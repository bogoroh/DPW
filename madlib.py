name = raw_input("What is your name? ") #String
day = raw_input("What day is it? ") #String
sunny = raw_input("Is it sunny? (Yes/No) ") #String
currency = float(raw_input("What is the current currency of Euro to US Dollar? (Hint=1.36) ")) #Float 
money = int(raw_input("How much money did he find? Please fill in a whole number in Euros ")) #Number

#Ammount he found in US Dollar
dollar = money * currency


#If statement for the opening sentence to check if it's sunny or not
if sunny == "Yes":
    opening = "It was a sunny"
else:
    opening = "It was a grimy"
    
#Casino Game
casinoGames = ["poker","roulette","blackjack","slots","craps"]
import random
#Find out what game we are playing
gameIndex = random.randrange(0,5)
#Hold the string for the casinoGames
casinoGame = casinoGames[gameIndex]

#Bartender 
bartender = {"Vanessa":"1800 Silver Dog","Britney":"Abbot's Dream","Jessica":"Apple Daiquiri","Nicole":"Bangkok Bomb"}
import random
randomName = random.choice(bartender.keys()) #Grabs a random string from the dictionary 
bartenderDrink = bartender[randomName] #Uses the variable to call out the value of the key 

message = '''{opening} {day}. The ducks were swimming and it looked like a nomal day at work for {name}. After work {name} was walking to his car and found a wallet with {money} Euro in it. The following day he went to the bank and converted his Euros into dollars with the rate of {currency} per Euro. {name} got {dollar} out of it and decided to go the casino and try his luck with the money he found. When he arrived at the casino he got greeted by his favorite bartender Vanessa with her favorite drink called: {bartenderDrink}. He made his way to the {casinoGame} room and decided to try all his luck there. '''
messageFormatted = message.format(**locals())

print messageFormatted