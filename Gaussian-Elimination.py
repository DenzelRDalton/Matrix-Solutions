A_Matrix = [
    [1, 0, 2, 1],
    [2, -1, 3, -1],
    [4, 1, 8, 2]
]

n = len(A_Matrix)


def check_for_reorder(num_col):
    # Initialize values
    max_col_value = abs(A_Matrix[num_col][num_col])
    max_col_index = num_col

    for i in range(num_col, n):
        # If we have found a larger value record that value, and it's index
        if abs(A_Matrix[i][num_col]) > max_col_value:
            max_col_index = i
            max_col_value = abs(A_Matrix[i][num_col])

    # If we found a larger value swap the rows
    if max_col_index > num_col:
        temp = A_Matrix[num_col]
        A_Matrix[num_col] = A_Matrix[max_col_index]
        A_Matrix[max_col_index] = temp


for i in range(n):
    # Check if rows need swapping
    check_for_reorder(i)
    for j in range(i, n):
        # Make sure we are looking at a different column and that it is non-zero
        if A_Matrix[j][i] != 0 and i != j:
            # Init subtraction vector
            subtraction_vector = []
            for x in range(n+1):
                # Multiply through row to get lower triangular matrix
                subtraction_vector.append((A_Matrix[j][i]/A_Matrix[i][i]) * A_Matrix[i][x])
            for k in range(len(subtraction_vector)):
                # Subtract through row to get lower triangular matrix
                A_Matrix[j][k] -= subtraction_vector[k]

# Init values for x vector
init_value = A_Matrix[n-1][n] / A_Matrix[n-1][n-1]
found_value_vector = [None] * n
found_value_vector[n-1] = init_value

# Back substitution
for i in range(n-2, -1, -1):
    found_value_vector[i] = A_Matrix[i][n]
    for j in range(i+1, n):
        found_value_vector[i] = found_value_vector[i] - A_Matrix[i][j] * found_value_vector[j]
    found_value_vector[i] = found_value_vector[i]/A_Matrix[i][i]

print("The values of the x vector are: ")
for x in found_value_vector:
    print(x)
