# Exercise 1

# Character Input

#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extras:

#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


name = input("Hi! Please tell me your name and press Enter: \n")

age = int(input("Hi " + name + ". How old are you? "))
year = 2017 + 100 - age
finalmessage = "You will turn 100 in the year " + str(year) + ". \n"
print(finalmessage)
number = int(input("Give me a number: "))

print(number * finalmessage)