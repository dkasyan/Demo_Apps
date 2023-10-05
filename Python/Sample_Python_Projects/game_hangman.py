import random

random_words = ["noga", "car", "epileptyka"]
empty_list = []
special_word = random.choice(random_words)

guess = input("Guess a letter: ").lower()

for i in special_word:
    empty_list.append("_")
    if guess == i:
        print("OK")
    else:
        print("Wrong")
print(empty_list)

#print(f"Is this what you just said? {choice}")

