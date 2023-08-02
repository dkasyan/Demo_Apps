import random

random_words = ["noga", "car", "epileptyka"]
special_word = random.choice(random_words)
choice = "b"
for letter in special_word:
    if letter == choice:
        print("OK")



def covered_fields(special_word):

    print(len(special_word))

covered_fields(special_word)
#print(f"Is this what you just said? {choice}")

