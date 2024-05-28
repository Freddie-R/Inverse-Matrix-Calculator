def get_inverse(matrix,determinant):
    inverse = []
    for row in range(len(matrix)):
        inverse_row = []
        for collum in range(len(matrix)):
            inverse_row.append((matrix[row][collum])/determinant)
        inverse.append(inverse_row)
    return inverse