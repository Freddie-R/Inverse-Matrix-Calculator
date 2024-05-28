def check_val(integer,is_float):
    if is_float:
        #check if the interger is a float
        try:
            value = float(integer)
            #if we have an float we return the value
            return value
        except ValueError:
            #if the value can't be cast to an integer we ask for another integer
            print("Please enter a valid number")
            return "null"
    else:
        #check if the input is an integer 
        try:
            value = int(integer)
            if value < 1:
                #if needed we check if the integer is less than 1 and if it is we ask for another input
                print("Please enter a value greater than 0")
                return "null"
            #if we have an integer we return the value
            return value
        except ValueError:
            #if the value can't be cast to an integer we ask for another integer
            print("Please enter a valid integer")
            return "null"


def create_matrix():
    size = "null"
    while size == "null":
        #ask for the size of the matrix until you have a postive interger
        size = check_val(input("Enter the size of your square matrix: "),False)
    
    #define the original matrix
    matrix = []

    for i in range(size):
        #create a new row
        row =[]

        for j in range(size):
            value = 'null'
            #for each valye in each row assign a value
            while value == 'null':
                value = check_val(input(f"Enter the value for cell ({i},{j}): "),True)
            #append that value to the row
            row.append(value)

        #append the row to the matrix
        matrix.append(row)

    #return the matrix
    return matrix