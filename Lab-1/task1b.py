# task1b
task1b_input = open(file='input1b.txt', mode='r')

task1b_output = open(file='output1b.txt', mode='w')

num_of_line = int(task1b_input.readline())

for i in range(num_of_line):
    temp = task1b_input.readline().strip().split(" ")

    if temp[2]== "+" :
        add = int(temp[1]) + int(temp[3])
        s = f"The result of {temp[1]} {temp[2]} {temp[3]} is {add}.\n"
        task1b_output.write(s)
    elif temp[2]== "-" :
        sub = int(temp[1]) - int(temp[3])
        s = f"The result of {temp[1]} {temp[2]} {temp[3]} is {sub}.\n"
        task1b_output.write(s)
    elif temp[2]== "*" :
        mul = int(temp[1]) * int(temp[3])
        s = f"The result of {temp[1]} {temp[2]} {temp[3]} is {mul}.\n"
        task1b_output.write(s)
    elif temp[2]== "/" :
        div = int(temp[1]) / int(temp[3])
        s = f"The result of {temp[1]} {temp[2]} {temp[3]} is {div}.\n"
        task1b_output.write(s)

task1b_input.close()
task1b_output.close()