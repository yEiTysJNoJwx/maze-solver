from random import shuffle

rows, columns = 15, 15
maze = [[' ' for _ in range(columns)] for _ in range(rows)]

directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]

def generate_maze(x, y):
    maze[y][x] = '■'
    shuffle(directions)

    for move_x, move_y in directions:
        new_x, new_y = x + move_x, y + move_y
        if 1 <= new_x <= columns - 1 and 1 <= new_y <= rows - 1 and maze[new_y][new_x] == ' ':
            maze[y + move_y // 2][x + move_x // 2] = '■'
            generate_maze(new_x, new_y)

# MARK: - TESTS

generate_maze(1, 1)
print('Maze 1 successfully generated. ✅')

for row in maze:
    for cell in row:
        print(cell, end = '')
    print('\n')

assert input('Review: ') == 'y'

