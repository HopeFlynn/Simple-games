# Simple Quiz Game

print("🎓 Welcome to the Quiz Game!")
print("Answer the following questions:\n")

questions = [
    {"question": "What is the capital of Kenya?", "options": ["Nairobi", "Kisumu", "Mombasa"], "answer": "Nairobi"},
    {"question": "Which language is used for structuring web pages?", "options": ["Python", "HTML", "Java"], "answer": "HTML"},
    {"question": "What does CPU stand for?", "options": ["Central Processing Unit", "Computer Power Unit", "Control Panel Unit"], "answer": "Central Processing Unit"},
]

score = 0

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(f"- {opt}")
    answer = input("Your answer: ").strip()
    
    if answer.lower() == q["answer"].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Oops! The correct answer is: {q['answer']}\n")

print(f"🎉 You got {score} out of {len(questions)} questions right!")

# Optional: Ask to replay
replay = input("Do you want to play again? (yes/no): ").strip().lower()
if replay == "yes":
    print("\nRestart the game to play again!")
else:
    print("Thanks for playing! 👋")
