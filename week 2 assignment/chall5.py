#Create a program that stores a list of words. 
# Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

# Step 1: Store a list of words
words = ["apple", "banana", "cherry", "date", "kiwi", "melon"]

# Step 2: Use list comprehension to filter words with odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Step 3: Print the new list of words with odd character lengths
print("Words with an odd number of characters:", odd_length_words)
