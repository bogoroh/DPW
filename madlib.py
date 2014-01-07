name = input("What is your name? Remember to type in Quotes")

day = input("What day is it? Remember to type in Quotes")

money = input("How much money did he find? Please fill in a whole number")

sunny = input("Is it sunny? (Yes/No) Remember to type in Quotes")

#If statement for the opening sentence to check if it's sunny or not
if sunny == "Yes":
    opening = "It's a sunny"
else:
    opening = "It's a grimy"
    
#Casino Game
casinoGame = ["Poker","Roulette","Blackjack","Slots","Craps"]
    
#Bartender 
bartender = {"Vanessa":"1800 Silver Dog","Britney":"Abbot's Dream","Jessica":"Apple Daiquiri","Nicole":"Bangkok Bomb"}

message = '''{opening} {day}. The ducks were swimmming and it looked like a nomal day at work for {name}. After work {name} was walking to his car and found a wallet with ${money} in it. {name} Decided to go the casino and try his luck with the money he found. When he arrived at the casino he got greeted by his favorite bartender vanessa with her favorite drink called bartender["Vannessa"]   '''
messageFormatted = message.format(**locals())

#print messageFormatted