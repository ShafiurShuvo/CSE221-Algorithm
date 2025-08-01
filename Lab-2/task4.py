#task4
def find_max(arr, start, end):
    if start == end:
        return arr[start]

    mid = (start + end) // 2
    max_left = find_max(arr, start, mid)
    max_right = find_max(arr, mid + 1, end)

    if max_left > max_right:
        return max_left
    else:
        return max_right

task4_input = open('input4.txt', 'r')
task4_output = open('output4.txt', 'w')

length = int(task4_input.readline())
numbers = list(map(int, task4_input.readline().split()))

max_value = find_max(numbers, 0, length - 1)

task4_output.write(str(max_value))

task4_input.close()
task4_output.close()