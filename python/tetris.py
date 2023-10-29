# Tetris Series #2 — Primitive Gameplay
# arr = ['1R4']
arr = ['1R4', '2L3', '3L2', '4L1', '1L0', '2R1', '3R2', '4R3', '1L4']
matrix = [[0 for _ in range(9)] for _ in range(32)]
cols = {'L4': 0, "L3": 1, "L2": 2, "L1": 3,
        "L0": 4, "R0": 4, "R1": 5, "R2": 6, "R3": 7, "R4": 8}

score = 0


def place(position):
    long = int(position[0])
    col = int(cols[position[1:]])
    if matrix[long][col] == 1:
        print("game over")
        return
    # print(f"{long} largo, {col} columna")
    for i in range(32):
        if matrix[31-i][col] == 0:
            # print(f"{i}row{col}column")
            for size in range(long):
                matrix[31-i-size][col] = 1
            return


def check_line(matrix):
    global score
    for i, row in enumerate(matrix):
        row_sum = sum(row)
        if row_sum == 9:
            score += 1
            # matrix[row] = [0] * 9
            push_down(i)
    return


def push_down(i):
    for row in range(i, 0, -1):
        matrix[row] = matrix[row - 1]
    matrix[0] = [0] * 9


def tetris(arr) -> int:

    for i in arr:
        place(i)
        check_line(matrix)

    return score


print(f"Score: {tetris(arr)}")
for row in matrix:
    print(row)
