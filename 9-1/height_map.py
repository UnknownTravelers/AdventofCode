file_data = []

with open("file.txt", 'r') as lines:
    for line in lines:
        file_data.append([int(s) for s in line[:-1] if s.isdigit()])

x_max = len(file_data[0])
y_max = len(file_data)

def is_local_min(x, y):
    h = file_data[y][x]
    out = True
    if x != 0:
        out = out and file_data[y][x-1] > h
    if y != 0:
        out = out and file_data[y-1][x] > h
    if x != x_max-1:
        out = out and file_data[y][x+1] > h
    if y != y_max-1:
        out = out and file_data[y+1][x] > h
    return out

sum_risk = 0
for j in range(0, len(file_data)):
    for i in range(0, len(file_data[0])):
        if is_local_min(i, j):
            sum_risk += 1 + file_data[j][i]

print(sum_risk)