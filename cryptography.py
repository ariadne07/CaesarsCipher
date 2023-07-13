import string

# Global variables
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
pos = []
mode = False
output = ""


#Make list of possible characters 
for x in characters:
    pos.append(x)

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters: " + characters + "\n\nLet's get started!\n")

#Recieve user input
msg = input("Type your message > ")
key = int(input("Input your key (between 0 and 93 inclusive) > " ))
done = False
while done == False:
    action = input("Encrypt or decrypt? > ").lower()
    if action == "encrypt":
        mode = True
        done = True
    elif action == "decrypt":
        mode = False
        done = True
    else:
        print("I didn't get that. Please try again.")

# Convert msg to index string 
index = []
for x in msg:
    for y in pos:
        if x == y:
            index.append(pos.index(y))

# Encrypt or decrypt the message
if mode:
    for x in index:
        if (x + key) >= len(pos):
            wrap = (x + key) - len(pos)
            output += pos[wrap]
        else:
            output += pos[x + key]
else: 
    for x in index:
        output += pos[x - key]

# Print the shifted message
print("Your " + action + "ed message is: " + output)
