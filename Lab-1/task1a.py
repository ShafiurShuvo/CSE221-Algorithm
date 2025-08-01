# task1a

task1a_input = open(file='input1a.txt', mode='r')
task1a_output = open(file='output1a.txt', mode='w')

num_of_line = int(task1a_input.readline())

for i in range(num_of_line):
    temp = int(task1a_input.readline())
    if(temp%2==0):
        s = f"{temp} is an Even Number.\n"
        task1a_output.write(s)
    else:
        s = f"{temp} is a Odd Number.\n"
        task1a_output.write(s)

task1a_input.close()
task1a_output.close()