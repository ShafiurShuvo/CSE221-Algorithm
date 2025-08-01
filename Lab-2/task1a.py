#task 1a
task1a_input = open('input1a.txt','r')
task1a_output = open('output1a.txt','w')

len_sum = (task1a_input.readline()).split(" ")
temp = (task1a_input.readline()).split(" ")

sum = False
for i in range(int(len_sum[0])-1):
    for j in range(i+1, int(len_sum[0])-1):
        if int(temp[i]) + int(temp[j]) == int(len_sum[1]):
            s = f"{i+1} {j+1}\n"
            task1a_output.write(s)
            sum = True


if sum is False:
    s = "IMPOSSIBLE\n"
    task1a_output.write(s)

task1a_input.close()
task1a_output.close()

# 6 18
# 9 10 1 5 9 8