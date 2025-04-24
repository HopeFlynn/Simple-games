# Random Joke Generator

import random
import time

jokes = [
    "Why did the Python programmer go hungry? Because his food was in bytes!",
    "Why do Java developers wear glasses? Because they can't C#!",
    "What do you call 8 hobbits? A hobbyte.",
    "I told my computer I needed a break, and it said 'No problem – I'll go to sleep.'"
]

print("🤣 Welcome to the Random Joke Generator!")

time.sleep(1)
print("Here's a joke for you:\n")

# Wait and display the joke for effect
time.sleep(1.5)
print(random.choice(jokes))
