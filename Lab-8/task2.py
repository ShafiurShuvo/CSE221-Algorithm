#task2
task2_input = open('input2_4.txt',"r")
task2_output = open('output2_4.txt',"w")

N = int(task2_input.readline())

def fibonacci(n):
    if n < 2:
        return n

    x = [0] * (n+1)
    x[0] = 1
    x[1] = 1

    for i in range(2, n+1):
        x[i] = x[i-1] + x[i-2]

    # print(x)
    return x[n]


x = fibonacci(N)
# print(x)
task2_output.write(str(x) )
task2_input.close()
task2_output.close()