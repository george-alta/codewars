def tetris(arr) -> int:
    matrix = [[0 for _ in range(9)] for _ in range(30)]
    cols = {'L4': 0, "L3": 1, "L2": 2, "L1": 3, "L0": 4,
            "R0": 4, "R1": 5, "R2": 6, "R3": 7, "R4": 8}
    score = 0

    def place(position):
        long = int(position[0])
        col = int(cols[position[1:]])
        for i in range(30):
            if matrix[29 - i][col] == 0:
                for size in range(long):
                    if 29 - i < size:
                        return
                    else:
                        matrix[29 - i - size][col] = 1
                return

    def check_line(matrix):
        nonlocal score
        for i, row in enumerate(matrix):
            row_sum = sum(row)
            if row_sum == 9:
                score += 1
                push_down(i)

    def push_down(i):
        for row in range(i, 0, -1):
            matrix[row] = matrix[row - 1]
        matrix[0] = [0] * 9

    for i in arr:
        place(i)
        check_line(matrix)

    return score
