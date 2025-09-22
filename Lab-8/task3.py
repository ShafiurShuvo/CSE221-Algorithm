#task3
task3_input = open('input3_2.txt',"r")
task3_output = open('output3_2.txt',"w")

N, X = map(int, task3_input.readline().split())
coins = list(map(int, task3_input.readline().split()))


def min_coins(coins, num):
    v = float('inf')
    list1 = [0] + [v] * num
    # print(list1)
    for i in range(1, num + 1):
        for j in coins:
            if i - j >= 0:
                list1[i] = min(list1[i], list1[i - j] + 1)

                # print(list1)

    if list1[num] != v:
        return list1[num]
    else:
        return -1

result = min_coins(coins, X)
print(result)
task3_output.write(str(result))
task3_input.close()
task3_output.close()