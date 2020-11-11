import random
from turtle import *
import time

setup(width = 500, height = 200, startx =-200, starty = -600)

tokens = 1500
print("Welcome to Turtle Casino lets play Turtle Slots!")
print("Your balance is currently $"+str(tokens)+"!")

shape1 = Turtle()
shape2 = Turtle()
shape3 = Turtle()

shape1.setheading(90)
shape2.setheading(90)
shape3.setheading(90)

shape1.up()
shape2.up()
shape3.up()

shape1.goto(-100,0)
shape3.goto(100,0)

shapelist = ["square", "circle", "triangle"]


while True:
    print("welcome to turtle slots")
    while tokens > 0:
        print("You Have", tokens, "tokens.")
        try: 
            bet = int(input("Bet amount: "))
        except:
            print("Please enter a whole number of tokens.")
            continue
        for i in range(3):
            shape1.shape(shapelist[i])
            time.sleep(0.1)
            shape2.shape(shapelist[i])
            time.sleep(0.1)
            shape3.shape(shapelist[i])
            time.sleep(0.1)
        
        if bet > tokens:
            print("Not enough tokens.")
        else:
            tokens -= bet
            result1 = random.choice(shapelist)
            shape1.shape()
            result2 = random.choice(shapelist)
            shape2.shape()
            result3 = random.choice(shapelist)
            shape3.shape()


        if result1 == result2 and result2 == result3:
            amountwon = bet * 2
            print("You won", amountwon, "tokens")
            tokens += amountwon
        else:
            print("You lost this time.")  
print("You are out of tokens")  
print("Thank you for playing")
