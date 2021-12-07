from statistics import median

file_data = []

with open("file.txt", 'r') as lines:
    for line in lines:
        file_data = [int(s) for s in line.split(',') if s.isdigit()]

# resolve for median
target = median(file_data)
print(target)
c = 0
for p in file_data:
    c += abs(p-target)

print(c)