'''
Title: Love calculator
write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
'''

print("Welcome to the Love calculator")
name1= input("what is your name?")
name2= input("what is their name?")
#making the inpout lower case
name1= name1.lower()
name2 = name2.lower()

#checking number of letters in the word TRUE
t=name1.count("t") + name2.count("t")
r=name1.count("r") + name2.count("r")
u=name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")
true = t+r+u+e

#checking num of letters in the word LOVE
l= name1.count("l") + name2.count("l")
o= name1.count("o") + name2.count("o")
v= name1.count("v") + name2.count("v")
e1 = name1.count("e") + name2.count("e")
love = l+o+v+e1
#converting true and love to str
true =str(true)
love =str(love)
#total score
score= int(true + love)
#setting conditions
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score>=40 and score<=50:
    print(f"Your score is {score},you are alright together.")
else:
    print(f"Your score is {score}")