# find the submatrix of a given matrix (remove the row and collum)
def get_submatrix(matrix,row,collum):
    submatrix =[]
    for i in range(len(matrix)):
        if i != collum:
            new_row=[]
            for j in range(len(matrix)):
                if j != row:
                    new_row.append(matrix[i][j])
            submatrix.append(new_row)
    return submatrix

list1=get_submatrix([[4,3,2],[5,3,2],[8,7,6]],1,1)

print(list1)