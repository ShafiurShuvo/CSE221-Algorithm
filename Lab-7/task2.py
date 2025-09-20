#task2
task2_input = open('input2_2.txt', 'r')
task2_output = open('output2_2.txt', 'w')

N, M = map(int, task2_input.readline().split(' '))

tasks = []
for i in range(N):
    S, E = list(map(int, task2_input.readline().split()))
    tasks.append((S, E))

tasks.sort(key=lambda x: x[1], reverse = True)
print(tasks)

list_1 = []
list_2 = []

for i in range(M):
    end_time = float('inf')
    for j in range(i, len(tasks)):
        if tasks[j][1] <= end_time:
            if tasks[j] not in list_1:
                list_1.append(tasks[j])
                end_time = tasks[j][0]
for i in range(len(tasks)):
      if tasks[i] not in list_2 and tasks[i] not in list_1:
                list_2.append(tasks[i])

task2_output.write(str(max(len(list_1), len(list_2))))

task2_input.close()
task2_output.close()