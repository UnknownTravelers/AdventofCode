from statistics import mean
from math import floor, ceil

file_data = []

with open("file.txt", 'r') as lines:
    for line in lines:
        t = line[:-1].split('|')
        file_data.append([s.split(" ") for s in t])


occ_1_4_7_8 = 0
size = [2, 4, 3, 7]

for data in file_data:
    for e in data[1]:
        if len(e) in size:
            occ_1_4_7_8 += 1

print(occ_1_4_7_8)