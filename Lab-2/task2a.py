#task2a
def sort(arr1,arr2):
    new_arr = arr1 + arr2
    for i in range(len(new_arr)):
        new_arr[i]=int(new_arr[i])
    new_arr.sort()
    return new_arr

task2a_input = open("input2a.txt", "r")
task2a_output = open("output2a.txt", "w")
M = int(task2a_input.readline())
Alice = (task2a_input.readline()).split(" ")
N = int(task2a_input.readline())
Bob = (task2a_input.readline()).split(" ")

new_arr = sort(Alice,Bob)
print(new_arr)

s = " ".join(map(str, new_arr))
task2a_output.write(s)

task2a_input.close()
task2a_output.close()