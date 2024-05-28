#find the submatrix of a given matrix (remove the row and collum)
def get_submatrix(matrix,row,collum):
    #define the original matrix
    submatrix =[]
    #run through the matrix rows
    for i in range(len(matrix)):
        #check if chosen row then exclude
        if i != row:
            new_row=[]
            for j in range(len(matrix)):
                #check if chosen collum then exclude
                if j != collum:
                    new_row.append(matrix[i][j])
            #create the sub matrix
            submatrix.append(new_row)
    #return the submatrix
    return submatrix

#find the determiant
def get_determiant(matrix):
    #if the matrix is only one long then the determiant is itself
    if len(matrix)==1:
        return matrix[0][0]
    #if the matrix is 2 long then it can be solved using ad-bc
    elif len(matrix)==2:
        return (matrix[0][0]*matrix[1][1])-(matrix[1][0]*matrix[0][1])
    #when it is larger we loop the deterimiant function
    else:
        det = 0
        sign=1
        #run through each collum
        for collum in range(len(matrix)):
            #find the submatrix of each collum 
            submatrix = get_submatrix(matrix,0,collum)
            det += sign*matrix[0][collum]*get_determiant(submatrix)
            sign = sign*-1
    return det

#function to caculate the matrix of minors
def get_matrix_of_minors(matrix):
    #create a new list for the minors
    minors=[]
    #run through the rows and collums
    for row in range(len(matrix)):
        minor_row=[]
        for collum in range(len(matrix)):
            #find the determinant for each submatrix and append it to the list of minors
            submatrix = get_submatrix(matrix,row,collum)
            minor_determinant = get_determiant(submatrix)
            minor_row.append(minor_determinant)
        minors.append(minor_row)
    #return the matrix of minors
    return minors