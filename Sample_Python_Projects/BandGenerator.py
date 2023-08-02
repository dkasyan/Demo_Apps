def ask_questions():
    answer_list = []
    print("Welcome to the Band Name Generator.")
    x = input("What's name of the city you grew up in?\n: ")
    y = input("What is the name of a pet?\n: ")
    answer_list.append(x)
    answer_list.append(y)
    return answer_list
    
def band_gen_funct(answer_list):
    x = answer_list[0]
    y = answer_list[1]

    print("Your band name could be " + x + " "+ y)

    

answer_list = ask_questions()

band_gen_funct(answer_list)
