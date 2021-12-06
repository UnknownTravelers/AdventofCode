file_data = []

with open("file.txt", 'r') as lines:
    for line in lines:
        t = [s.split(',') for s in [q for q in line[:-1].split(' ')] if s != "->"]
        for e in t:
            e[0] = int(e[0])
            e[1] = int(e[1])
        file_data.append(t)
        
w, h = 1000, 1000
grid = [[0 for y in range(h)] for x in range(w)]

for data in file_data:
    x1 = data[0][0]
    x2 = data[1][0]
    y1 = data[0][1]
    y2 = data[1][1]
    if x1 == x2:
        x = x1
        for y in range(min(y1, y2), max(y1, y2)+1):
            grid[x][y] += 1
    elif y1 == y2:
        y = y1
        for x in range(min(x1, x2), max(x1, x2)+1):
            grid[x][y] += 1
    else:
        x2 += 1 if (x1 < x2) else -1
        y2 += 1 if (y1 < y2) else -1
        for i, j in zip(range(x1, x2, 1 if x1 < x2 else -1), range(y1, y2, 1 if y1 < y2 else -1)):
            grid[i][j] += 1

cross = 0
for x in range(0, w):
    for y in range(0, h):
        if grid[x][y] > 1:
            print(x, y, grid[x][y])
            cross += 1

# with open('out.txt', 'w') as fd:
    # for x in range(0, w):
        # for y in range(0, h):
            # fd.write(str(grid[x][y]))
        # fd.write("\n")

print(cross)