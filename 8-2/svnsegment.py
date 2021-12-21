from statistics import mean
from math import floor, ceil

file_data = []

with open("file.txt", 'r') as lines:
    for line in lines:
        t = line[:-1].split('|')
        file_data.append([s.split(" ") for s in t])

def inter(a, b):
    out = []
    for l in a:
        if l in b:
            out.append(l)
    return out

def substraction(a, b):
    out = []
    for l in a:
        if not l in b:
            out.append(l)
    for l in b:
        if not l in a:
            out.append(l)
    return out

def union(a, b):
    out = []
    for l in a:
        out.append(l)
    for l in b:
        if not l in out:
            out.append(l)
    return out
    

size = [2, 4, 3, 7]
out_sum = 0
for data in file_data:
    e_sure = [0]*10
    s_sure = [0]*7
    liste_2_3_5 = []
    liste_0_6_9 = []
    for e in data[0]:
        if len(e) == 2:
            e_sure[1] = e
        elif len(e) == 3:
            e_sure[7] = e
        elif len(e) == 4:
            e_sure[4] = e
        elif len(e) == 5:
            liste_2_3_5.append(e)
        elif len (e) == 6:
            liste_0_6_9.append(e)
        elif len(e) == 7:
            e_sure[8] = e
        
    # find 3 in 2_3_5 => 2 & 5 has 3 common seg while 2 & 3 and 3 & 5 has 4
    if len(inter(liste_2_3_5[0], liste_2_3_5[1])) == 3:
        e_sure[3] = liste_2_3_5[2]
    elif len(inter(liste_2_3_5[0], liste_2_3_5[2])) == 3:
        e_sure[3] = liste_2_3_5[1]
    else:
        e_sure[3] = liste_2_3_5[0]

    # now we know 1, 3, 4, 7 & 8
    # we can learn 'a' with 7 - 1
    # s_sure[0] = substraction(e_sure[7], e_sure[1]) # not used to find numbers
    # we can learn 'b' with 4 - (3 inter 4)
    s_sure[1] = substraction(e_sure[4], inter(e_sure[3], e_sure[4]))
    # we can learn 'd' with (3 inter 4) - 1
    s_sure[3] = substraction(inter(e_sure[3], e_sure[4]), e_sure[1])
    # we can learn 'e' with 8 - (3 + 4)
    s_sure[4] = substraction(union(e_sure[4], e_sure[3]), e_sure[8])
    # we can learn 'g' as 3 - 1 - ('a' + 'd')
    # s_sure[6] = substraction(substraction(e_sure[3], e_sure[1]), [s_sure[0], s_sure[3]]) # not used to find numbers
    
    # for 'c' and 'f' we will need 6 or 9, but we want 
    for e in liste_2_3_5:
        if len(inter(e, s_sure[1])) == 1:
            e_sure[5] = e
        elif len(inter(e, s_sure[4])) == 1:
            e_sure[2] = e
    
    for e in liste_0_6_9:
        if len(inter(e, s_sure[3])) == 0:
            e_sure[0] = e
        elif len(inter(e, s_sure[4])) == 0:
            e_sure[9] = e
        else:
            e_sure[6] = e
    
    # next is how to get final segments, but has no use for the exercice
    # to get 'c' is 8 - 6
    # s_sure[2] = substraction(e_sure[8], e_sure[6])
    # to get 'f' is 8 - 9
    # s_sure[5] = substraction(e_sure[8], e_sure[9])
    
    def find_number(elem, e_sure):
        for i in range(0, 10):
            if len(substraction(elem, e_sure[i])) == 0:
                return i
    
    out = 0
    for e in data[1]:
        if len(e) != 0:
            out *= 10
            out += find_number(e, e_sure)
    out_sum += out


print(out_sum)