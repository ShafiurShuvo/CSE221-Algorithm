#task3

task3_input = open('input3_2.txt', 'r')
task3_output = open('output3_2.txt', 'w')

N, K = map(int,task3_input.readline().split())

parent_list = [0]*(N+1)
for i in range(len(parent_list)):
    parent_list[i] = i

# print(parent_list)

tree = {}

for i in range(1,N+1):
    tree[i] = {i}

for i in range(K):
    A, B = map(int,task3_input.readline().split())

    parent = parent_list[A]
    child = parent_list[B]

    for i in tree[child]:
        tree[parent].add(i)
        parent_list[B] = A
        # print(parent_list)

    result = len(tree[parent])
    # print(result)
    task3_output.write(str(result) + '\n')

print(tree)
task3_input.close()
task3_output.close()