# Logie A. Mendiola | BSCPE 1-5 | Object Oriented Programming | P-3

# Write a method in python to write multiple line of text contents into a text file mylife.txt

#Created variable to store contents to the text file
# with open("mylife.txt", "a+") as my_File:

# #
#     for line in my_File:
#         line_placement = line

#         random_thoughts = input("What's on your mind today? ")
#         additional_thoughts = input("Would you like to say something more? Yes or No:")

#         if additional_thoughts == "Yes" or "yes" or "y" or "Y":
#             random_thoughts = line_placement
#             my_File.write(my_File + "\n")
        
#         elif additional_thoughts == "No" or "no" or "n" or "N":
#             break

#         else:
#             print("Please try again")

with open("mylife.txt", "a+") as my_File:
    option_yes = "yes"
    option_no = "no"
    option_y = "y"
    option_n = "n"
    additional_thoughts = "yes"

    while additional_thoughts.lower() != option_no and additional_thoughts.lower() != option_n:
        if additional_thoughts.lower() == option_yes or additional_thoughts.lower() == option_y: 
            random_thoughts = input("What's on your mind today? ")
            my_File.write(random_thoughts + "\n")
        else:
            print("Please try again")
        
        
        additional_thoughts = input("Would you like to say something more? Yes or No: ")
        print(additional_thoughts)
    
