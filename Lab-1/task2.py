# task2
task2_input = open('input2.txt','r')
task2_output = open('output2.txt','w')

len_of_arr = int(task2_input.readline().strip())
arr = (task2_input.readline().split(" "))

for i in range(len_of_arr-1):
    swap = False
    for j in range(len_of_arr-i-1):
        if int(arr[j]) > int(arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap = True

    if not swap:
        break

#s = " ".join(map(str, arr))
for i in range(len_of_arr):
    task2_output.write(arr[i]+" ")

task2_input.close()
task2_output.close()