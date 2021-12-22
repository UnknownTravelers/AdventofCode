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
        return 1
    elif c == ']':
        return 2
    elif c == '}':
        return 3
    elif c == '>':
        return 4

def get_string_score(str):
    out = 0
    for c in str:
        out *= 5
        out += get_score(c)
    return out
    
scores = []
for line in file_data:
    construction_string = []
    corrupted = False
    for c in line:
        if is_open(c):
            construction_string += c
        elif c == get_close(construction_string[-1]):
            construction_string = construction_string[:-1]
        else:
            corrupted = True
            break;
    if not corrupted:
        line_completion = ""
        for c in construction_string:
            line_completion = get_close(c) + line_completion
        scores.append(get_string_score(line_completion))


scores.sort()
print(scores[int(len(scores)/2)])