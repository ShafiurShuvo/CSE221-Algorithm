#task 3
def Partition(arr, start, end):
    pivot = arr[end]
    idx = start - 1

    for i in range(start, end):
        if arr[i] <= pivot:
            idx += 1
            arr[idx], arr[i] = arr[i], arr[idx]

    arr[idx + 1], arr[end] = arr[end], arr[idx + 1]

    return idx + 1

def QuickSort(arr, start, end):
    if start < end:
        pivotIndex = Partition(arr, start, end)
        QuickSort(arr, start, pivotIndex - 1)
        QuickSort(arr, pivotIndex + 1, end)
    else:
        return arr

task3_input = open('input3.txt', 'r')
task3_output = open('output3.txt', 'w')

length = int(task3_input.readline())
arr = list(map(int, task3_input.readline().split()))
QuickSort(arr, 0, len(arr) - 1)

task3_output.write(" ".join(map(str, arr)))

task3_input.close()
task3_output.close()