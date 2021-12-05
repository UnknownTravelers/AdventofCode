file_data = []


with open("file.txt", 'r') as lines:
    for line in lines:
        t = line.split(' ')
        t[1] = int(t[1])
        file_data.append(t)

x = 0
depth = 0

for data in file_data:
    if data[0] == "forward":
        x += data[1]
    elif data[0] == "up":
        depth -= data[1]
    elif data[0] == "down":
        depth += data[1]
    else :
        print(data[0] + " ?")
        
print("x : " + str(x) + "; depth : " + str(depth))