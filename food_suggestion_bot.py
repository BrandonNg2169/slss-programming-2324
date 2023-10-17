A bot that asks the user what their favourite food is. The bot identifies the type/cuisine of the 
food and offer a suggestion for a restaurent 

import random 
import time 


# Introduce the bot to user
# ask the author what their favourite food is 
print("Hello I am here to suggest a restaurant to you")
time.sleep(1) 
fave_food = input("To help suggest a restaurant, tell me what ur favourite foood is ?")
time.sleep(1)

# if they answer with an Itallian dish 
# Suggest an Inalian restaurant
# list all the italian dishes 
italian_food = ["pizza" , "pasta" , "cannelon"] 
if fave_food. lower.().strip(",.?! ") in italian_food: 
print ("I think you might like Italian food.")
time.sleep(1)
print("You can find the address below")
print("8836 Alexandra Rd, Richmond")
else 
print ("Sorry, I dont have suggestion on this dish ")
