# task4
task4_input = open('input4.txt','r')
task4_output = open('output4.txt','w')

trains = int(task4_input.readline().strip())

arr = []
for i in range(trains):
    temp = task4_input.readline().strip().split(" ")
    arr.append(temp)

# print(arr)

for i in range(len(arr)-1):
    for j in range(len(arr) - i - 1):
        if arr[j][0] > arr[j + 1][0]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if arr[j][1] > arr[j + 1][1]:
                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

        elif arr[j][0] == arr[j + 1][0]:
            p = arr[j][-1].split(":")
            min1 = int(p[0])*60 + int(p[1])
            q = arr[j + 1][-1].split(":")
            min2 = int(q[0])*60 + int(q[1])
            if min1 < min2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for i in arr:
    s = " ".join(map(str,i))
    task4_output.write(s+"\n")

task4_input.close()
task4_output.close()