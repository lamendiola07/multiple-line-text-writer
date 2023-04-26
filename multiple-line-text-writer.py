# Logie A. Mendiola | BSCPE 1-5 | Object Oriented Programming | P-3

# Write a method in python to write multiple line of text contents into a text file mylife.txt

# Extra codes for design
import pyfiglet
from simple_colors import *

print(magenta("~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~"))
print(yellow(pyfiglet.figlet_format("Task # 4: P-3", font = "3x5" )))
print(magenta("~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~~ooOo~"))

print(blue("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HELLO USER! WELCOME BACK TO OUR SYSTEM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))
print(blue("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TODAY WE WILL CREATE A PROGRAM TO WRITE MULTIPLE LINE TEXT ON TXT FILES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))
print(green("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ READY TO GO? ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))
print(green("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ - - - INITIATING SEQUENCE - - - ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))


#Created variable to store contents to the text file
with open("mylife.txt", "a+") as my_File:
    option_yes = "yes"
    option_no = "no"
    option_y = "y"
    option_n = "n"
    additional_thoughts = "yes"

# Write multiple lines of context
    while additional_thoughts.lower() != option_no and additional_thoughts.lower() != option_n:
        if additional_thoughts.lower() == option_yes or additional_thoughts.lower() == option_y: 
            random_thoughts = input("What's on your mind today? ")
            my_File.write(random_thoughts + "\n")
        else:
            print("Please try again")
        
        
        additional_thoughts = input("Would you like to say something more? Yes or No: ")
        print(additional_thoughts)
    
