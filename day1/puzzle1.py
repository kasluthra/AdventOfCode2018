data_file = open("input.txt", "r")

#This function reads and understands the input file into a usable form and structure 
def parse(lines):
    return lines

#The purpose of this function is to solve the puzzle with the input structure 
def solve(data):

    total_fuel = 0

    for x in range(len(data)):
        fuel_x = (int(data[x])//3) - 2
        total_fuel += fuel_x

    print(total_fuel)
    return -1
    
data = parse(data_file.readlines())
get_answer = solve(data)
