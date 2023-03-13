A_Matrix = [
    [1, -1,  0],
    [-2, 2, -1],
    [0,  1, -2]
]

n = len(A_Matrix)
num_swaps = 0


def check_for_reorder(num_col, num_swaps):
    # Initialize values
    max_col_value = abs(A_Matrix[num_col][num_col])
    max_col_index = num_col

    for i in range(num_col, n):
        # If we have found a larger value record that value, and it's index
        if abs(A_Matrix[i][num_col]) > max_col_value:
            max_col_index = i
            max_col_value = abs(A_Matrix[i][num_col])

    if max_col_index > num_col:
        # If we found a larger value swap the rows increment and return num_swaps
        temp = A_Matrix[num_col]
        A_Matrix[num_col] = A_Matrix[max_col_index]
        A_Matrix[max_col_index] = temp
        num_swaps += 1
    return num_swaps


for i in range(n):
    # Check for swaps
    num_swaps = check_for_reorder(i, num_swaps)
    for j in range(i, n):
        # Make sure we are looking at a different column and that it is non-zero
        if A_Matrix[j][i] != 0 and i != j:
            # Init subtraction vector
            subtraction_vector = []
            for x in range(n):
                # Multiply through row to get lower triangular matrix
                subtraction_vector.append((A_Matrix[j][i]/A_Matrix[i][i]) * A_Matrix[i][x])
            for k in range(len(subtraction_vector)):
                # Subtract through row to get lower triangular matrix
                A_Matrix[j][k] -= subtraction_vector[k]
# Init u_det
u_det = 1
for x in range(n):
    for j in range(n):
        if x == j:
            # Find product of diagonal values
            u_det *= A_Matrix[x][j]
            print(u_det)
# Find if 1 is negative
neg = pow(-1, num_swaps)
# Multiply the u_det by our 1 value
det = u_det * neg
# Print results
print("The determinant of the matrix A is: " + str(det))

