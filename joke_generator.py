import random  # Step 1: Import the random module

# Step 2: Create a list of jokes
jokes = [
    "Why do Python programmers prefer dark mode? Because light attracts bugs!",
    "Why do programmers hate nature? It has too many bugs.",
    "How do you tell HTML from HTML5? By the doctype!",
    "Why do Java developers wear glasses? Because they don’t see sharp.",
    "What is a programmer's favorite hangout place? Foo Bar!",
    "Why do programmers prefer iOS development? Because they can’t handle Android's Java runtime!",
    "What do you call a programmer from Finland? Nerdic!",
    "Why was the developer unhappy at their job? They wanted arrays but got stuck with a string!",
    "How many programmers does it take to change a light bulb? None; it’s a hardware problem!",
    "Why did the programmer quit their job? Because they didn’t get arrays!",
    "What’s a programmer’s favorite snack? Microchips!",
    "Why was the JavaScript developer sad? Because they didn’t know how to 'null' their feelings!",
    "What do you get when you cross a computer and a lifeguard? A screensaver!",
    "Why did the developer go broke? Because they used up all their cache!",
    "How do you comfort a JavaScript bug? You console it!"
]
# Step 3: Select a random joke
random_joke = random.choice(jokes)  # Choose a random joke from the list

# Step 4: Display the joke
print(random_joke)