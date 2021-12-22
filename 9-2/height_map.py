from math import prod

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

class Visit:
    
    def __init__(self, p=None):
        if p != None:
            self.explored = [p]
            self.len = 1
        else:
            self.explored = []
            self.len = 0
    
    def add(self, p):
        if (p in self.explored):
            return
        self.explored.append(p)
        self.len += 1
    
    def get_size(self):
        return self.len
    
    def contains(self, p):
        return p in self.explored
    
    def get_list(self):
        return self.explored
        
    def __lt__(self, v):
        return self.len < v.get_size()
        
    def __str__(self):
        return str(self.len)
    
    def __repr__(self):
        return str(self.len)
    

def find_bassin_size(to_explore, explored, in_bassin):
    next_to_explore = Visit()
    for p in to_explore.get_list():
        explored.add(p)
        
        if file_data[p[1]][p[0]] < 9:
            in_bassin.add(p)
        
            if p[0] != 0 and not explored.contains([p[0]-1, p[1]]):
                next_to_explore.add([p[0]-1, p[1]])
            if p[0] != x_max - 1 and not explored.contains([p[0]+1, p[1]]):
                next_to_explore.add([p[0]+1, p[1]])
            if p[1] != 0 and not explored.contains([p[0], p[1]-1]):
                next_to_explore.add([p[0], p[1]-1])
            if p[1] != y_max - 1 and not explored.contains([p[0], p[1]+1]):
                next_to_explore.add([p[0], p[1]+1])
    
    if next_to_explore.get_size() != 0:
        return find_bassin_size(next_to_explore, explored, in_bassin)
    return in_bassin

bassin_size = []
vizu = []
for j in range(0, len(file_data)):
    for i in range(0, len(file_data[0])):
        if is_local_min(i, j):
            o = find_bassin_size(Visit(p=[i, j]), Visit(), Visit())
            bassin_size.append(o.get_size())
            vizu.append(o)

vizu.sort()
print(vizu)
for v in vizu:
    if v.get_size() == 1051:
        print(v.get_list())

for v in vizu[-3:]:
    with open("vizu/out"+str(v.get_size())+".txt", "w+") as fd:
        for i in range(0, x_max):
            for j in range(0, y_max):
                if v.contains([i, j]):
                    fd.write("#")
                else:
                    fd.write(".")
            fd.write("\n")