import random
from turtle import *
import time
setup(width = 500, height = 200, startx =-200, starty = -600)

wallet = 1500



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

keep_playing = "true"

while keep_playing == "true":
  print("You have", wallet, "points to wager.")
  wager = int(input("What is your wager?"))
  if wager > wallet:
      continue
  wallet = wallet - wager
  for i in range(3):
      shape1.shape(shapelist[i])
      time.sleep(0.1)
      shape2.shape(shapelist[i])
      time.sleep(0.1)
      shape3.shape(shapelist[i])
      time.sleep(0.1)

result1 = random.choice(shapelist)
shape1.shape(result1)
result2 = random.choice(shapelist)
shape2.shape(result2)
result3 = random.choice(shapelist)
shape3.shape(result3)

if result1 == result2 and result2 == result3:
    if result1 == "square":
        print ("YOU ARE GREAT! WINNER 3 SQUARES!")
        wager = wager * 5
        wallet = wallet + wager
    elif result1 == "circle":
        print ("YOU ARE GREAT! WINNER 3 CIRCLES!")
        wager = wager * 15
        wallet = wallet + wager
    elif result == "triangle":
        print ("YOU ARE GREAT! WINNER 3 TRIANGLES")
        wager = wager * 20
        wallet = wallet + wager
    else:
        print ("LOSER SPEND MORE MONEY AND TRY AGAIN :D")








# welcome(wallet, pot)
#   choice = user_choice()
#   flip_result = coin_flip()
#   wallet = payment(wallet, -5)
#   overall_result = test_result(choice, flip_result)
#   wallet = wallet_resolution(wallet, overall_result, pot)
#   result_text(overall_result)
#   play_again(wallet, original_amount)
