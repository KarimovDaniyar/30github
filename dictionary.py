import random
import os
number = random.randint(1, 10)
quess = input("guess a number between 1 and 10: ")
quess = int(quess)
if (quess == number):
    print("you got it")
else:
    path = r'C:\Users\ACER\Desktop\chech'
    if os.path.exists(path):
        os.remove(path)
        print("File removed successfully.")
    else:
        print("File does not exist.")
        