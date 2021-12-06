file_data = []

with open("file.txt", 'r') as lines:
    for line in lines:
        file_data = [int(s) for s in line.split(',') if s.isdigit()]

lifespan = [0]*9

for l in file_data:
    lifespan[l] += 1


end_simul = 256
cpls = [0]*9

for days in range(0, end_simul):
    cpls = [0]*9
    cpls[8] += lifespan[0]
    cpls[6] += lifespan[0] + lifespan[7]
    cpls[7] += lifespan[8]
    cpls[5] += lifespan[6]
    cpls[4] += lifespan[5]
    cpls[3] += lifespan[4]
    cpls[2] += lifespan[3]
    cpls[1] += lifespan[2]
    cpls[0] += lifespan[1]
    lifespan = cpls
    
print(lifespan)
print(sum(lifespan))