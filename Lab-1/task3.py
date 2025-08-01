# task3
task3_input = open('input3.txt','r')
task3_output = open('output3.txt','w')
num_of_line = int(task3_input.readline())
id = task3_input.readline().split(" ")
mark = task3_input.readline().split(" ")
arr = []
for i in range(len(mark)):
    mark[i] = int(mark[i])
    id[i] = int(id[i])
    tup = (mark[i],id[i])
    arr.append(tup)
print(arr)

def selectionSort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j][0] > arr[min_idx][0]:
                min_idx = j
            elif arr[j][0] == arr[min_idx][0]:
                if arr[j][1] < arr[min_idx][1]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    for i in range(len(arr)):
        s = f"ID: {arr[i][1]} Mark: {arr[i][0]}\n"
        task3_output.write(s)

selectionSort(arr)

task3_input.close()
task3_output.close()