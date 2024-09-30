import webbrowser
import os
import time
from datetime import datetime

current_time = datetime.now().strftime("%m/%d/%y %I:%M")

print("Welcome to the Basic Notes Program")
name = input("What do you want to name your file: ")
name += ".txt"
print(f"{name} created.")
status = True

with open(name, "a") as file:
    while status:
        ask1 = input("What do you want us to save? ")
        file.write(f"{current_time}: {ask1}\n")
        print(f"{datetime.now().strftime("%m-%d %I:%M")}: Request Successful") 
        while True:
            choice = input("Did you want us to save anything else: ").upper()
            if choice == "YES":
                break
            elif choice == "NO":
                print("Program stopped")
                status = False
                break
            else:
                print("Please response with \"Yes\" or \"No\"")
