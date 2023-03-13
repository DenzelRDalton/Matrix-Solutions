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
    # Divide through the row at i by the diagonal value to get 1 on the diagonal
    A_Matrix[i] = [x / A_Matrix[i][i] for x in A_Matrix[i]]
    for j in range(n):
        # Make sure we are looking at a different column and that it is non-zero
        if A_Matrix[j][i] != 0 and i != j:
            # Init subtraction vector
            subtraction_vector = []
            for x in range(n+1):
                # Multipy through the row by the value we are targeting
                subtraction_vector.append(A_Matrix[j][i] * A_Matrix[i][x])
            for k in range(len(subtraction_vector)):
                # Subtract to eliminate the value we are targeting
                A_Matrix[j][k] -= subtraction_vector[k]

# Print results
print("The resulting matrix from Gauss-Jordan Elimination is: ")
for x in A_Matrix:
    print(x)
