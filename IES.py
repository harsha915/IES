#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
def roll_dice():
    min_value = 1
    max_value = 6
    while True:
        dice_number = random.randint(min_value, max_value)
        print("You rolled:", dice_number)
        roll_again = input("Do you want to roll the dice again? (yes/no): ")
        if roll_again.lower() == "yes" or roll_again.lower() == "y":
            continue  
        else:
            break  
print("Welcome to the Roll the Dice game!")
roll_dice()


# In[ ]:




