# task3
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    a1 = arr[:mid]
    a2 = arr[mid:]

    a1 = merge_sort(a1)
    a2 = merge_sort(a2)

    merged_arr = merge(a1, a2)

    return merged_arr


def merge(a, b):
    merged_arr = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged_arr.append(a[i])
            i += 1
        else:
            merged_arr.append(b[j])
            j += 1

    while i < len(a):
        merged_arr.append(a[i])
        i += 1

    while j < len(b):
        merged_arr.append(b[j])
        j += 1

    return merged_arr

arr = [8, 1, 4, 2, 1, 3]
sorted_arr = merge_sort(arr)
print(sorted_arr)

task3_input = open('input3.txt', 'r')
task3_output = open('output3.txt', 'w')

length = int(task3_input.readline())
list1 = task3_input.readline().split()

merged_arr = merge_sort(list1)

s = " ".join(merged_arr)
task3_output.write(s)

task3_input.close()
task3_output.close()