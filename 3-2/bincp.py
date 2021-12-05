file_data = []

with open("file.txt", 'r') as lines:
    for line in lines:
        t = list(line[:-1])
        for i in range(0, len(t)):
            t[i] = int(t[i])
        file_data.append(t)

def filter_most(arr, i):
    if i >= len(arr[0]):
        return arr[0]
    ones = 0
    zeros = 0
    one_arr = []
    zero_arr = []
    for elem in arr:
        if elem[i] == 1:
            ones += 1
            one_arr.append(elem)
        else:
            zeros += 1
            zero_arr.append(elem)
    if ones >= zeros:
        return filter_most(one_arr, i+1)
    else:
        return filter_most(zero_arr, i+1)

def filter_least(arr, i):
    if i >= len(arr[0]):
        return arr[0]
    ones = 0
    zeros = 0
    one_arr = []
    zero_arr = []
    for elem in arr:
        if elem[i] == 1:
            ones += 1
            one_arr.append(elem)
        else:
            zeros += 1
            zero_arr.append(elem)
    print("", ones, one_arr, "\n", zeros, zero_arr, "\n")
    if (ones > 0 and zeros > 0) and zeros <= ones or (ones == 0 and zeros > 0):
        return filter_least(zero_arr, i+1)
    elif (ones > 0 and zeros > 0) or ones < zeros or (ones > 0 and zeros == 0):
        return filter_least(one_arr, i+1)
    else:
        print(zeros, ones, "?")
        return [0]

most = filter_most(file_data, 0)
least = filter_least(file_data, 0)

def bin_to_int(bit_arr):
    out = 0
    for bit in bit_arr:
        out *= 2
        out += bit
    return out
print(most, bin_to_int(most))
print(least, bin_to_int(least))