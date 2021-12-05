file_data = []
draw = []

with open("file.txt", 'r') as lines:
    ln = 0
    grid = []
    for line in lines:
        ln += 1
        if ln == 1:
            draw = [int(s) for s in line[:-1].split(',') if s.isdigit()]
        else:
            if (ln+3)%6 == 4:
                # final line
                t = [int(s) for s in line.split() if s.isdigit()]
                grid.append(t)
                file_data.append(grid)
            elif (ln+3)%6 == 5:
                # empty line
                grid = []
            else:
                t = [int(s) for s in line.split() if s.isdigit()]
                grid.append(t)

def has_completed(data):
    completed = []
    for grid in data:
        col_check = [True]*5
        row_check = [True]*5
        for i in range(0, 5):
            for j in range(0, 5):
                if grid[i][j] != -1:
                    row_check[i] = False
                    col_check[j] = False
        if col_check == [False]*5 and row_check == [False]*5:
            completed.append(False)
        else:
            completed.append(True)
    return completed

def draw_number(data, n):
    for grid in data:
        for i in range(0, 5):
            for j in range(0, 5):
                if grid[i][j] == n:
                    grid[i][j] = -1

last_n = -1
for n in draw:
    last_n = n
    draw_number(file_data, n)
    completed = has_completed(file_data)
    if any(completed):
        break

boards = [grid for c, grid in zip(completed, file_data) if c]

def grid_sum(grid):
    sum = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if grid[i][j] != -1:
                sum += grid[i][j]
    return sum

print(grid_sum(boards[0]))
print(n)