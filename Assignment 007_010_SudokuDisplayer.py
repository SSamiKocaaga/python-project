sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
dashdash = ''
for i in range(15):
    dashdash = dashdash + '- '
for i in range(len(sudoku)):
    counter = 1
    if i % 3 == 0:
        print(dashdash)
    for j in range(len(sudoku[i])):
        if counter % 3 != 0:
            print(sudoku[i][j], end='  ')
        elif counter % 3 == 0 and counter < 9:
            print(sudoku[i][j], end='  | ')
        elif counter == 9:
            print(sudoku[i][j], end=' \n')
        counter += 1
print(dashdash)