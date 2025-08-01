#task4
task4_input = open('input4.txt','r')
task4_output = open('output4.txt','w')
 
length = int(task4_input.readline())
arr = list(map(int,task4_input.readline().split()))
test = int(task4_input.readline())

def Partition(arr, start, end):
    pivot = arr[end]
    idx = start - 1

    for i in range(start, end):
        if arr[i] <= pivot:
            idx += 1
            arr[idx], arr[i] = arr[i], arr[idx]

    arr[idx + 1], arr[end] = arr[end], arr[idx + 1]

    return idx + 1

def find_kth_smallest(arr,k):
    small = 0
    large = len(arr) - 1

    while True:
        pivot = Partition(arr, small, large)
        if pivot == k - 1:
            return arr[pivot]
        elif pivot > k - 1:
            large = pivot - 1
        else:
            small = pivot + 1


for i in range(test):
    kth_val = int(task4_input.readline())
    result = str(find_kth_smallest(arr, kth_val))
    task4_output.write(result + '\n')
task4_input.close()
task4_output.close()