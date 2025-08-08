#task1b
task1b_input = open('input1b_3.txt', 'r')
task1b_output = open('output1b_3.txt', 'w')

vertices, edges = map(int, task1b_input.readline().split())

adjacency_list = {i: [] for i in range(vertices+1)}

while edges > 0:
    row, column, cost = map(int, task1b_input.readline().split())

    adjacency_list[row].append((column, cost))
    edges -= 1

for vertex, neighbors in adjacency_list.items():
    store_str = f"{vertex} :"
    for neighbor, cost in neighbors:
        store_str += f" ({neighbor},{cost})"
    task1b_output.write(store_str + "\n")

task1b_input.close()
task1b_output.close()
