name = raw_input("What is your name? ") #String
day = raw_input("What day is it? ") #String
sunny = raw_input("Is it sunny? (Yes/No) ") #String
currency = float(raw_input("What is the current currency of Euro to US Dollar? (Hint=1.36) ")) #Float 
money = int(raw_input("How much money did he find? Please fill in a whole number in Euros ")) #Number
celcius = int(raw_input("What is the weather in degrees Celcius? ")) #Number
tax = int(raw_input("How much percent do you have to pay taxes?(0-100) ")) #Number

#Ammount he found in US Dollar (1st mathematical operator)
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
bartenderDrink = bartender["Vanessa"]

#Dice
import random
#Find out what number you threw
dice = random.randrange(1,7) #Dice randomg numbers 1,2,3,4,5,6

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

#first function calculating his new bank roll with the earnings
def bankBalance():
    balance = 6000
    earnings = 1200
    balance += earnings #Assignement operator
    return balance
bankF =  bankBalance()

#Figure out how much money he is left with after taxes
if tax < 100: #Mathematical Operator
    taxPercent = 0.45 # you pay 55% of taxes
elif tax < 60:
    taxPercent = 0.50 # you pay 50% of taxes
elif tax < 40:
    taxPercent = 0.60 # you pay 40% of taxes  
elif tax < 20:
    taxPercent = 0.75 # you pay 25% of taxes
else:
    taxPercent = 0.90 # you pay 10% of taxes
netto = bankF * taxPercent #Money he is left with after taxes

#Second function
def temperature(celcius):
    fahrenheit = 9.0 / 5.0 * celcius + 32 # Mathematical operator
    return fahrenheit #Number in fahrenheit

# Variable for the temperature converter
temperatureF = temperature(celcius)
    
message = '''{opening} {day} with a temperature of {temperatureF} degrees Fahrenheit. The ducks were swimming and it looked like a nomal day at work for {name}. After work {name} was walking to his car and found a wallet with {money} Euro in it. The following day he went to the bank and converted his Euros into dollars with the rate of {currency} per Euro. {name} got {dollar} out of it and decided to go the casino and try his luck with the money he found. When he arrived at the casino he got greeted by his favorite bartender Vanessa with her favorite drink called: {bartenderDrink}. He was also the 10000th player to enter the casino that game and was allowed to throw a dice to see if he won a bonus. He threw the dice and {diceMoney}. He made his way to the {casinoGame} room and decided to try his luck there. Not too much luck but he left the casino with some profit. It was getting close to new year so he decided to go outside and see the fireworks. He looked at the clock and saw there was only 10 minutes remaining for New year. He kept looking down at his watch counting down. '''
messageFormatted = message.format(**locals())

print messageFormatted
for countDown in reversed([0,1,2,3,4,5,6,7,9,10]): # Loop reversing the countdown in the array till new year 
    timeNewYear = countDown, "Minutes left till new year"
    print timeNewYear # countdown timer till new year
    if countDown == 0:
        newYear = "Happy new year !!!"
        print newYear
message2 = '''He celebrated with some chapagne and a dance with his favorite bartender and decided to take a cab back home since it got pretty late. The next morning when he woke up with so much money he had to go the bank and deposit some of it. So he did that and wanted to see how much money he still had on his account. His receipt gave him {bankF}. He had to withdraw all that money to pay his taxes. For this year he had to pay {tax}% of his total bankroll on taxes. Leaving him with {netto}$.   '''
messageFormatted2 = message2.format(**locals())

print messageFormatted2