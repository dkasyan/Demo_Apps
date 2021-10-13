def ask_questions():
    answer_list = []
    x = input("Your City:\n")
    y = input("Your pet:\n")
    answer_list.append(x)
    answer_list.append(y)
    return answer_list
    
def band_gen_funct(answer_list):
    x = answer_list[0]
    y = answer_list[1]
    print(x + " "+ y)

    

answer_list = ask_questions()

band_gen_funct(answer_list)

#band_gen_funct()