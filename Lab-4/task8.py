#task8
task_input = open('input8.txt', 'r')
task_output = open('output8.txt', 'w')

T = int(task_input.readline().strip())

for case in range(1, T+1):
    n = int(task_input.readline().strip())

    adj = {}
    for i in range(n):
        u, v = [int(x) for x in task_input.readline().strip().split()]
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)

    visited = {}
    color = {}  # 1 or 2 for two sides
    ans = 0

    def bfs(start):
        queue = [start]
        visited[start] = 1
        color[start] = 1
        front = 0
        count1 = 1  # number in color1
        count2 = 0  # number in color2

        while front < len(queue):
            node = queue[front]
            front += 1
            this_color = color[node]
            for neigh in adj[node]:
                if neigh not in visited:
                    visited[neigh] = 1
                    
                    if this_color == 1:
                        color[neigh] = 2
                        count2 += 1
                    else:
                        color[neigh] = 1
                        count1 += 1
                    queue.append(neigh)
        return max(count1, count2)

    for node in adj.keys():
        if node not in visited:
            ans += bfs(node)

    task_output.write(f"Case {case}: {ans}\n")

task_input.close()
task_output.close()