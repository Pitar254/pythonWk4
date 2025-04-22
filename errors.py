# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

try:
    file = open("noFile.txt", "r") 
    data = file.read()
    print("The data is: ", data)
except FileNotFoundError:
    print("Sorry, This file does not exist.")