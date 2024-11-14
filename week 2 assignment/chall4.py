#Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.



# Step 1: Accept user input to create two sets of integers
set1 = set(map(int, input("Enter integers for the first set (space-separated): ").split()))
set2 = set(map(int, input("Enter integers for the second set (space-separated): ").split()))

# Step 2: Find the intersection of both sets (common elements)
common_elements = set1 & set2

# Step 3: Print the new set containing common elements
print("The common elements between the two sets are:", common_elements)
