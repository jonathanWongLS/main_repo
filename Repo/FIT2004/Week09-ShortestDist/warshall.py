
# initialise adjacency matrix
matrix = []
count_vertex = None

# if matrix[i,j] = True and matrix[j,k] = True then matrix[i,k] = True
for k in range(count_vertex):
    for i in range(count_vertex):
        for j in range(count_vertex):
            matrix[i][j] = matrix[i,j] or (matrix[i][k] and matrix[k][j])