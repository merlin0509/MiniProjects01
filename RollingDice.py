import numpy as np
def roll():
  dice=np.random.randint(1,7)
  print("You rolled a : ", dice)
  if dice==6:
    YN = bool(input("Do you want to roll again? True or False \n"))
    if (YN==True):
      roll()
roll()
