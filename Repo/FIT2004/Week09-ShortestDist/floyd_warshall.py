for k in range(count_vertex):
    for i in range(count_vertex):
        for j in range(count_vertex):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])