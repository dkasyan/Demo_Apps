program_list = []
program_square_list = []
program = [ program_list.append(element) for element in range(105) if element % 5 == 0]
print(program_list)
program_square = [program_square_list.append(element ** 3) for element in program_list]
print(program_square_list)