# Create a program that reads a file and writes a modified version to a new file.
file = open("week4.txt", "r") # open the file in read mode
data = file.read() # read the file

print(data)

# Create a new file and write the modified data to it
new_file = open("week4_new.txt", "w") # open the file in write mode
new_file.write(data) # write the data to the new file


