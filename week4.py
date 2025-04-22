# 1a. Create a program that reads a file and writes a modified version to a new file.
file = open("week4.txt", "r") # open the file in read mode
data = file.read() # read the file

print(data)

# 1b. Create a new file and write the modified data to it
new_file = open("week4_new.txt", "w") # open the file in write mode
new_file.write(data) # write the data to the new file


# 2. Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
try:
    file = open("noFile.txt", "r") 
    data = file.read()
    print("The data is: ", data)
except FileNotFoundError:
    print("Sorry, This file does not exist.")


