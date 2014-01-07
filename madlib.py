name = input("What is your name? Remember to type in Quotes")

day = input("What day is it? Remember to type in Quotes")
sunny = input("Is it sunny? (Yes/No) Remember to type in Quotes")
currency = input("What is the current currency of Euro to US Dollar? (Hint=1.36) ")
money = input("How much money did he find? Please fill in a whole number in Euros")

#Ammount he found in US Dollar
dollar = money * currency

#If statement for the opening sentence to check if it's sunny or not
if sunny == "Yes":
    opening = "It's a sunny"
else:
    opening = "It's a grimy"
    
#Casino Game
casinoGame = ["Poker","Roulette","Blackjack","Slots","Craps"]
    
#Bartender 
bartender = {"Vanessa":"1800 Silver Dog","Britney":"Abbot's Dream","Jessica":"Apple Daiquiri","Nicole":"Bangkok Bomb"}

message = '''{opening} {day}. The ducks were swimmming and it looked like a nomal day at work for {name}. After work {name} was walking to his car and found a wallet with {money} Euro in it. The following day he went to the bank and converted his Euros into dollar with the rate of {currency} per euro.{name} got {dollar} out of it and decided to go the casino and try his luck with the money he found. When he arrived at the casino he got greeted by his favorite bartender vanessa with her favorite drink called: bartender["Vannessa"].    '''
messageFormatted = message.format(**locals())

#print messageFormatted