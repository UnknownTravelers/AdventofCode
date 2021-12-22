file_data = []

with open("file.txt", 'r') as lines:
    for line in lines:
        file_data.append(line[:-1])

pair = [
    ['(', ')'],
    ['[', ']'],
    ['{', '}'],
    ['<', '>']
]

def is_open(c):
    return c in ['(', '[', '{', '<']

def get_open(c):
    if c == ')':
        return '('
    elif c == ']':
        return '['
    elif c == '}':
        return '{'
    elif c == '>':
        return '<'

def get_close(c):
    if c == '(':
        return ')'
    elif c == '[':
        return ']'
    elif c == '{':
        return '}'
    elif c == '<':
        return '>'

def get_score(c):
    if c == ')':
        return 3
    elif c == ']':
        return 57
    elif c == '}':
        return 1197
    elif c == '>':
        return 25137
    
score = 0
for line in file_data:
    construction_string = []
    for c in line:
        if is_open(c):
            construction_string += c
        elif c == get_close(construction_string[-1]):
            construction_string = construction_string[:-1]
        else:
            score += get_score(c)
            break;

print(score)