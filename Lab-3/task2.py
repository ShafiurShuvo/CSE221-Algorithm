#task2
task2_input = open('input2.txt','r')
task2_output = open('output2.txt', 'w')

n = int(task2_input.readline())
arr = list(map(int, task2_input.readline().split()))

abs_arr = [0] * len(arr)

max_val = arr[0] + arr[1]**2
max_abs = 0

for i in range(len(arr)):
    abs_arr[i] = abs(arr[i])
for i in range(1,len(arr)):
    j = abs_arr[i]
    if j >= max_abs:
        max_abs = j
        idx = i
for i in range(idx):
    sum = arr[i] + max_abs**2
    if sum > max_val:
        max_val = sum

task2_output.write(str(max_val))
task2_input.close()
task2_output.close()