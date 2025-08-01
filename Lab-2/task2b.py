#task 2b
def merge(left, right):
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if int(left[i]) <= int(right[j]):
            sorted_list.append(int(left[i]))
            i += 1
        else:
            sorted_list.append(int(right[j]))
            j += 1

    while i < int(len(left)):
        sorted_list.append(int(left[i]))
        i += 1

    while j < int(len(right)):
        sorted_list.append(int(right[j]))
        j += 1

    # s = " ".join(map(str, sorted_list))
    return sorted_list


task2b_input = open('input2b.txt','r')
task2b_output = open('output2b.txt','w')

M = int(task2b_input.readline())
Alice = (task2b_input.readline()).split(" ")
N = int(task2b_input.readline())
Bob = (task2b_input.readline()).split(" ")
sorted_list = (merge(Alice, Bob))
# print(sorted_list)


s = " ".join(map(str, sorted_list))
task2b_output.write(s)

task2b_input.close()
task2b_output.close()