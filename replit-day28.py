import os, time, random

def character():
  varCharacter = input("Name Your Legend: ")
  print(varCharacter)

  varCharacterType = input("Character Type (Human, Elf, Wiard, Orc): ")
  print(varCharacterType)
  return varCharacter

def health():
  sixRoll = int(random.randint(1,6))
  twelveRoll = int(random.randint(1,12))

  varHealth = ((sixRoll * twelveRoll)/2)+10
  return varHealth

def strenght():
  strenghtSixRoll = int(random.randint(1,6))
  strenghtTwelveRoll = int(random.randint(1,12))

  varStrenght = ((strenghtSixRoll * strenghtTwelveRoll)/2)+12
  return varStrenght

print("BATTLE TIME\n")
time.sleep(1)

character1 = character()
health1 = health()
strenght1 = strenght()

print("\n",character1,"\n Health:",health1,"\n Strenght:",strenght1,"\n")

print("Who are you battling?\n")

character2 = character()
health2 = health()
strenght2 = strenght()

print("\n",character2,"\n Health:",health2,"\n Strenght:",strenght2,"\n")
time.sleep(5)

battleCounter = int(0)

while True:
  os.system('clear')

  print("BATTLE TIME\n")
  time.sleep(1)

  battleCounter += 1
  rollDice1 = random.randint(1,6)
  rollDice2 = random.randint(1,6)

  if rollDice1 > rollDice2:
    print(character1, "wins")
    print(character2, "takes a hit with ",strenght1, "damage\n")
    time.sleep(3)
    health2 = health2 - strenght1

    print(character1, "\n Health:", health1)
    print()
    print(character2, "\n Health:", health2)

    if health2 > 0:
      print()
      print("And they're both standing for the next round!")
      time.sleep(2)
      continue
    else:
      break
  elif rollDice2 > rollDice1:
    print(character2, "wins")
    print(character1, "takes a hit with ",strenght2, "damage\n")
    time.sleep(3)
    health1 = health1 - strenght2

    print(character1, "\n Health:", health1)
    print()
    print(character2, "\n Health:", health2)

    if health1 > 0:
      print()
      print("And they're both standing for the next round!")
      time.sleep(2)
      continue
    else:
      break
  else:
    print("It's a tie\n")
    time.sleep(2)
    continue

if health1 > 0:
  print(character2, "has died\n")
  print(character1, "wins in",battleCounter, "battles\n")
else:
  print(character1, "has died\n")
  print(character2, "wins in",battleCounter, "battles\n")