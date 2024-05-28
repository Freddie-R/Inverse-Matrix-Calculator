def get_matrix_of_cofactors(matrix):
    co_factors=[]
    sign = 1
    for row in range(len(matrix)):
        row_of_co_factors = []
        for collum in range(len(matrix)):
            row_of_co_factors.append(sign*matrix[row][collum])
            sign = sign*-1
        co_factors.append(row_of_co_factors)
    return co_factors