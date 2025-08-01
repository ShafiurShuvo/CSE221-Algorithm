#task 1b
task1b_input = open('input1b.txt','r')
task1b_output = open('output1b.txt','w')

len_sum = (task1b_input.readline()).split(" ")
temp = (task1b_input.readline()).split(" ")
ditc = {}
n1 = 0
n2 = 0

for i in range(len(temp)):
    ditc[i] = int(temp[i])

for j in range(len(temp)):
    x = int(len_sum[1]) - int(temp[j])
    if x in ditc.values():
        n1 = j+1
        break

for k in range(len(temp)):
    if int(temp[k]) == x and k != n1-1:
        n2 = k+1
        break

if n1 == 0 or n2 == 0:
    s = "IMPOSSIBLE"
    task1b_output.write(s)
else:
    s = f'{n1} {n2}'
    task1b_output.write(s)


task1b_input.close()
task1b_output.close()