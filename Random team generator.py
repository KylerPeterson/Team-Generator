import random
i = 0
j = 0
mylist = []
team1 = []
team2 = []


while True:
  name = input("Enter name: ")
  if (name != 'x'):
    mylist.append(name)
    continue
  break


print("Number of players: "+ str(len(mylist)))

print(mylist)
random.shuffle(mylist)
print(mylist)

team_size = len(mylist)/2
print("team 1: ")
while i < team_size:
  team1 = mylist.pop(0)
  i = i + 1
  
  print(team1)

print("team 2: ")
while j < team_size:
  team2 = mylist.pop(0)
  j = j + 1
  
  print(team2)

