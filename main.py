def which_direction():
  while True:
  go = input("Which way do you want to go, left or right? ")
    if go == "": continue
  go = go[0].lower()
  if go in ['l', 'r']:
      return go
    else:
      print("I don't understand")  
  return go
player = input("What's your name explorer? ")
print("Welcome to the Auror village,", player)
print()
print("You find yourself in a village")
print("You can see two villagers")
print("one attractive lady on the right, one old hag on the left")
go = which_direction()
if go == 'l':
   print("You have chosen to speak to the old hag")
if go == 'r':
   print("You have chosen to speak to the attractive lady")