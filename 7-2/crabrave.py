from statistics import mean

file_data = []

with open("file.txt", 'r') as lines:
    for line in lines:
        file_data = [int(s) for s in line.split(',') if s.isdigit()]

# resolve for mean
# target = round(mean(file_data))
# print(target)

def grow_add(n):
    out = 0
    for i in range(1, n+1):
        out += i
    return out

total_cons = []

for t in range(min(file_data), max(file_data)+1):
    c = 0
    for p in file_data:
        c += grow_add(abs(p-t))
    total_cons.append([t, c])

def min_kv(arr):
    min_k = arr[0][0]
    min_v = arr[0][1]
    for k, v in arr:
        if v < min_v:
            min_k, min_v = k, v
    return [min_k, min_v]

print(min_kv(total_cons))