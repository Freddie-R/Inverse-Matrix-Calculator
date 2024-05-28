from Initial_Inputs import *
from Determinant_And_Minors import *
from Matrix_Of_Co_Factors import *
from Transpose import *
from Inverse import *

def main():
    original_matrix = create_matrix()
    determiant = get_determiant(original_matrix)
    if determiant != 0:
        matrix_of_minors=get_matrix_of_minors(original_matrix)
        matrix_of_co_factors = get_matrix_of_cofactors(matrix_of_minors)
        transposed = get_transpose(matrix_of_co_factors)
        inverse = get_inverse(transposed,determiant)
        print("The determiant of your matrix is", determiant, "and the inverse to your matrix is:")
        for row in inverse:
            print(row)
    else:
        print("Your matrix's determiant is 0 meaning you have a singilar matrix with no inverse")

if __name__ == "__main__":
    main()