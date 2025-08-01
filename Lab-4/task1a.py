#task1a
task1a_input = open('input1a_2.txt','r')
task1a_output = open('output1a_2.txt', 'w')
vertices,edges = map(int,task1a_input.readline().split())

nested_list=[]
adjacency_matrix = [[0 for i in range(vertices + 1)] for i in range(vertices + 1)]

temp = 0
while temp < edges :
    row, column, cost = map(int,task1a_input.readline().split())

    adjacency_matrix[row][column]=int (cost)
    temp=temp+1

store_str=""
for a in adjacency_matrix :
    for i in a :
      store_str=store_str+ str(i)+' '
    task1a_output.write(store_str + "\n")
    store_str=""
task1a_input.close()
task1a_output.close()