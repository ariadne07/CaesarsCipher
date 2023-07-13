# code written for GWC Cryptography program
import string

#variables
possibleKey = 0
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
output = ""

#functions
def tryIt():
    global output
    output = ""
    for x in index:
        output += characters[x - possibleKey]
    return output 

#program 
print("Welcome! This program will crack the Caesar cipher and figure out any secret message that was encrypted with the Caesar cipher. Type in your encrypted message and this program will print all of the key possibilities of your message below. \n\nYour message can only include the following characters: " + characters + "\n\n")
msg = input("What is your encrypted message? > ")
input("\nPress enter to generate all of the key possibilities for your encrypted message.\n")

#make msg integer list 
index = []
for x in msg:
    for y in characters:
        if x == y:
            index.append(characters.index(y))

# cylcle through possible keys 
while possibleKey < len(characters):
    print("Key #" + str(possibleKey) + ": " + tryIt() + "\n")
    possibleKey += 1

