# Step 1: Define the quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    },
    {
        "question": "what is largest animal in the ocean?",
        "options": ["A) Shark", "B)Whale", "C)Blue whale", "D)Seal"],
        "answer": "C"
    }
]

def play_quiz():
    score = 0  # Initialize the score

    # Step 2: Loop through each question
    for q in questions:
        print(q["question"])  # Print the question
        for option in q["options"]:
            print(option)  # Print the options

        user_answer = input("Your answer (A/B/C/D): ").upper()  # Get user input and convert to uppercase

        # Step 3: Check if the answer is correct
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1  # Increase score
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")

    # Step 4: Show the final score
    print(f"Your final score is {score} out of {len(questions)}.")

# Step 5: Allow the user to play again
while True:
    play_quiz()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break

