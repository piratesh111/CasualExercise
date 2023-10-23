import random
from enum import Enum

def ApproximateValue(value):
    lowestValue = value - 0.1 * value
    highestValue = value + 0.1 * value
    return random.randint(lowestValue, highestValue)

yourMoney = 0
gameLength = 5
Event = Enum('Event', ['Chest', 'Nothing'])
eventDictionary = {
    Event.Chest: 0.6,
    Event.Nothing: 0.4
    }
Chests = Enum('Chests', {'Green': 4000,
                         'Orange':9000,
                         'Purple':14000,
                         'Golden':20000
                         })
chestsDictionary = {
    Chests.Green: 0.75,
    Chests.Orange: 0.20,
    Chests.Purple: 0.04,
    Chests.Golden: 0.01
    }
chestsList = tuple(chestsDictionary.keys())
chestsProbability = tuple(chestsDictionary.values())
eventList = list(eventDictionary.keys())
eventProbability = list(eventDictionary.values())                
while gameLength > 0:
    gameAnswer = input("Do you want move forward:")
    if gameAnswer == 'yes':
        print("u moved forward")
        DrawnEvent = random.choices(eventList, eventProbability)[0]
        if DrawnEvent == Event.Chest:
            print("u have found a chest")
            DrawnChest = random.choices(chestsList, chestsProbability)[0]
            foundGold = ApproximateValue(DrawnChest.value)
            print("in the chest u found:",Approximate, "gold")
            yourMoney = yourMoney + foundGold
            print("u have",yourMoney,"gold")
        elif DrawnEvent ==Event.Nothing:
            print("U got nothing my friend")       
    else:
        print("u can only go forward")
        continue
    gameLength -=1
print("Game is over you collected:",yourMoney, "coins")

     
    
