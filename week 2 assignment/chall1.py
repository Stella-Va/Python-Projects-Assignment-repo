#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

numbers = []

n = int(input("How many numbers would you like to input? "))

# Use a loop to accept the user's input and add it to the list
for i in range(n):
    num = int(input(f"Enter number {i+1}: ")) 
    numbers.append(num)  # Add the entered number to the list

#  sum of all the integers in the list
total_sum = sum(numbers)

print(f"The sum of all the numbers is: {total_sum}")
