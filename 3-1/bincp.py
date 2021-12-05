file_data = []

with open("file.txt", 'r') as lines:
    for line in lines:
        t = list(line[:-1])
        for i in range(0, len(t)):
            t[i] = int(t[i])
        file_data.append(t)

ones = [0]*len(file_data[0])
for i in range(0, len(file_data)):
    for j in range(0, len(file_data[i])):
        if file_data[i][j] == 1:
            ones[j] += 1 

result = []
for n in ones:
    result.append(1 if (n > len(file_data)/2) else 0)

complement = []
for bit in result:
    complement.append(0 if bit == 1 else 1)

def bin_to_int(bit_arr):
    out = 0
    for bit in bit_arr:
        out *= 2
        out += bit
    return out
print(bin_to_int(result))
print(bin_to_int(complement))