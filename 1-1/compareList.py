
increase = 0
p_line = 0
first_line = True
with open("file.txt", 'r') as lines:
  for line in lines:
    l = int(line)
    if not first_line:
      if p_line < l:
        increase += 1
    p_line = l
    first_line = False

print(increase)