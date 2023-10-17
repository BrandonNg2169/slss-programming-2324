 # star war bot 
 # author Brandon 
 # 17-10-23

print("I will decide if you can join the Dark Side.")

qt_1 = input ("Is red your favourite colour?")
qt_2 = input ("Do you like capes? ")

fave_colur = ("no")
like_capes = ("no")

fave_colur_an2 = ("yes", "no")
like_capes_an2 = ("yes", "no")

if qt_1.lower().strip(",.?!") in fave_colur and qt_2.lower().strip(",.?!") in like_capes:
    print("Light Side, I see. ")

elif qt_1.lower().strip(",.?!") in fave_colur_an2 and qt_2.lower().strip(",.?!") in like_capes_an2:
    print("Dark Side it is")

else:
    print ("Light Side, I see")