# Silahkan cari hasil dari pengurangan dari jumlah diagonal sebuah matrik NxN


def cal_diagonal_diff(input_matrix):
    num_row = len(matrix)
    for col in input_matrix:
        if(len(col) != num_row):
            return "error: Invalid matrix NxN"
    
    left_diagonal_sum = 0
    right_diagonal_sum = 0

    for i in range(num_row):
        left_diagonal_sum += input_matrix[i][i]

    print("left", left_diagonal_sum)
    for i in range(num_row):
        right_diagonal_sum += input_matrix[i][num_row - i - 1]

    print("right", right_diagonal_sum)
    return left_diagonal_sum - right_diagonal_sum

matrix = [
    [1, 2, 0],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_difference = cal_diagonal_diff(matrix)
print(diagonal_difference)