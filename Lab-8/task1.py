#task1
task1_input = open('input1_2.txt',"r")
task1_output = open('output1_2.txt',"w")

N, M = map(int, task1_input.readline().split())
graph = {i: [] for i in range(1, N + 1)}

for i in range(M):
    u, v, w = map(int, task1_input.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

print(graph)

total_cost = 0

source = 1
store = {source}

while len(store) < N:
    min_cost = float('inf')

    min_city = None

    for x in store:
        for k, v in graph[x]:
            if k not in store and  v < min_cost :
                min_cost= v
                min_city= k

    store.add(min_city)

    total_cost += min_cost

task1_output.write(str(total_cost) )
task1_input.close()
task1_output.close()