#!/usr/bin/python3
import  os
os.system('clear')
print("\n\nImported os\n\n")
def personal (name, age, col, py, world):
   import string
   print("\nYou have provided the following details:\n\tName: ",name,"\n\tAge: ",age,"\n\tFave colour: ",col,"\n\tPython preference: ",py,"\n\tFlat word: ",world)
   for character in name:
     if character not in string.ascii_letters :
       return print("\nYou are more than just a number, honestly, please try again!")
   if age > 99 or age < 3:
       print("\n"+ name + ", I really dont think your age is credible, do you?" )
   if col.upper()!="GREEN":
      print("\nI am really like green, but",col,"is OK!")
   else:
      print("\nI really like green too!")
   if py.upper()[0]!="Y":
      print("\nI am sorry that you dont like Python")
   else:
      print("\nGlad you agree that Python is cool..")
   if world != "False" :
      return print("\nEither you really Do think the world is flat (it isnt), \nor you havent tyed False in the correct Python format...\n\n")
   return "OK",print("\nAll OK, thanks a lot.")

details={}
details["Name"] = input("Hi, what is your name?")
details["Age"] = int(input("How old are you?"))
details["Colour"] = input("What is your favourite color?")
details["Python"] = input("dO you like Python?")
details["World"] = input("The world is flat: True or False?")
personal(*list(details.values()))
print("\n\nThis was the dictionary you set up...\n\n", details,"\n\nBye!\n\n")
