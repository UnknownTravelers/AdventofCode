w_size = 3
increase = 0
file_data = []
processed_data = []
first_line = True
with open("file.txt", 'r') as lines:
    for line in lines:
        file_data.append(int(line))

for i in range(0, len(file_data) - 2):
    processed_data.append(file_data[i] + file_data[i+1] + file_data[i+2])

for data in processed_data:
    if not first_line and p_line < data:
        increase += 1
    p_line = data
    first_line = False

print(increase)