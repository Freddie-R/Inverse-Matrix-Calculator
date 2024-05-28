def get_transpose(matrix):
    transposed = []
    for row in range(len(matrix)):
        transposed_row = []
        for collum in range(len(matrix)):
            transposed_row.append(matrix[collum][row])
        transposed.append(transposed_row)
    return transposed