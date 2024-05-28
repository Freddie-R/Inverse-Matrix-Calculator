Inverse Matrix Solver
This project contains a Python program to compute the inverse of a given square matrix. The process includes calculating the determinant, matrix of minors, matrix of co-factors, transpose of the co-factor matrix, and finally the inverse matrix.

Project Structure
Initial_Inputs.py: Contains functions to create and validate the input matrix.
Determinant_And_Minors.py: Contains functions to calculate the determinant and matrix of minors.
Matrix_Of_Co_Factors.py: Contains functions to compute the matrix of co-factors.
Transpose.py: Contains functions to transpose a matrix.
Inverse.py: Contains functions to compute the inverse of a matrix using the determinant and transposed co-factor matrix.
Main Program
The main program is defined in the main function which orchestrates the entire process. Here's a breakdown of the process:

Create Matrix:
Uses create_matrix function to take user input for a square matrix.
Matrix size and values are validated during input.

Calculate Determinant:
Uses get_determiant function to calculate the determinant of the matrix.

Check for Singular Matrix:
If the determinant is zero, the matrix is singular and has no inverse. An appropriate message is displayed.
If the determinant is non-zero, the program proceeds to calculate the inverse.

Calculate Inverse:
Matrix of Minors: Uses get_matrix_of_minors function.
Matrix of Co-factors: Uses get_matrix_of_cofactors function.
Transpose Matrix: Uses get_transpose function.
Inverse Matrix: Uses get_inverse function.

Display Result:
The determinant and inverse matrix are printed.

How to Run
1. Ensure all required files (Initial_Inputs.py, Determinant_And_Minors.py, Matrix_Of_Co_Factors.py, Transpose.py, Inverse.py, main.py) are in the same directory.
2. Run the main script:
3. Follow the prompts to enter the size and elements of the square matrix.

Dependencies
Python 3.x

Feel free to modify the code for additional functionality or improvements.
