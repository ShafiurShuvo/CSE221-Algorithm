#Task no 1
task1_input = open('input1.txt','r')
task1_output = open('output1.txt', 'w')
num = int(task1_input.readline())
arr = list(map(int,task1_input.readline().split(' ')))

def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr) // 2

        a1, l = mergeSort(arr[:mid])
        a2, r = mergeSort(arr[mid:])
        newarr = []
        count = l + r
        left = 0
        right = 0
        while left < len(a1) and right < len(a2):
            if (a1[left]) <= (a2[right]):
                newarr.append(a1[left])
                left = left + 1
            else:
                newarr.append(a2[right])
                right = right + 1
                count += len(a1) - left
        newarr += a1[left:] + a2[right:]
        return newarr , count
def pair_count(num, arr):
    maincount = mergeSort(arr)
    return maincount[1]

s = str(pair_count(num, arr))
task1_output.write(s)

task1_input.close()
task1_output.close()