name = raw_input("What is your name? ") #String
day = raw_input("What day is it? ") #String
sunny = raw_input("Is it sunny? (Yes/No) ") #String
currency = float(raw_input("What is the current currency of Euro to US Dollar? (Hint=1.36) ")) #Float 
money = int(raw_input("How much money did he find? Please fill in a whole number in Euros ")) #Number

#Ammount he found in US Dollar (1st mathematical operator)
dollar = money * currency


#How much money he went away with after tax
tax = 0.8 #He has to pay 20% to the government as tax
#total = * tax #2th Mathematical operator

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
bartenderDrink = bartender["Vanessa"]

#Dice
import random
#Find out what number you threw
dice = random.randrange(1,7)

if dice == 1 or dice == 6:
    diceMoney = "unfortunately he didn't win anything."
elif dice == 2:
    diceMoney = "he won 200$"
elif dice == 3:
    diceMoney = "he won 300$"
elif dice == 4:
    diceMoney = "he won 400$"
else:
    diceMoney = "he won 500$"

#first function
def bankBalance():
    balance = 6000
    earnings = 1200
    balance += earnings
    return balance

bankF =  bankBalance()

message = '''{opening} {day}. The ducks were swimming and it looked like a nomal day at work for {name}. After work {name} was walking to his car and found a wallet with {money} Euro in it. The following day he went to the bank and converted his Euros into dollars with the rate of {currency} per Euro. {name} got {dollar} out of it and decided to go the casino and try his luck with the money he found. When he arrived at the casino he got greeted by his favorite bartender Vanessa with her favorite drink called: {bartenderDrink}. He was also the 10000th player to enter the casino that game and was allowed to throw a dice to see if he won a bonus. He threw the dice and {diceMoney}. He made his way to the {casinoGame} room and decided to try his luck there. It was getting close to new year so he decided to go outside and see the fireworks. He looked at the clock and saw there was only 10 minutes remaining for New year. He kept looking down at his clock counting down. '''
messageFormatted = message.format(**locals())


print messageFormatted
for countDown in reversed([0,1,2,3,4,5,6,7,9,10]): # Loop reversing the countdown till new year
    timeNewYear = countDown, "Minutes left till new year"
    print timeNewYear
    if countDown == 0:
        newYear = "Happy new year !!!"
        
message2 = '''The next morning when he woke up with so much money he had to go the bank and deposit some of it. So he did that and wanted to see how much money he still had on his account. His receipt gave him {bankF} '''
messageFormatted2 = message2.format(**locals())


print messageFormatted2