#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console.

user_info = {
    "Name": "",
    "Age": "",
    "Favourite color": ""
}

user_info["Name"] = input("What's your name? ") 
user_info["Age"] = input("How old are you? ") 
user_info["Favourite color"] = input("What's your favourite color? ")

print(user_info)