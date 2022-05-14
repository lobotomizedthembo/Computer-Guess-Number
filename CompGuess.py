import time
import random
userNum = int(input("Please enter a number between 1 and 10: "))
counter = 0

while (True):
    compguess = random.randint(1, 10)
    print(compguess)
    time.sleep(1)
    counter = counter + 1
    if (compguess == userNum):
        break

print("It took the computer "+str(counter)+" tries")
