import random

random_words = ["noga", "car", "epileptyka"]
empty_list = []
special_word = random.choice(random_words)



for word in range(len(special_word)):
    print(len(special_word))
    guess = input("Guess a letter: ").lower()
    for i in special_word:
        if guess == i:
            empty_list.append(i)
        else:
            empty_list.append("_")
    print(empty_list)








#print(f"Is this what you just said? {choice}")

