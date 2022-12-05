from pzzl import pzzl

inp = pzzl(2,).strings()

plays = [tuple(el.split(' ')) for el in inp]

print(plays)
map = {'A': 1,
       'B': 2,
       'C': 3}


def rock_paper_scissors(play):
    x, y = play
    
    resp = {'X': 'A', 'Y': 'B', 'Z': 'C'}

    yy = resp[y]

    points=0

    if x == yy:
        return map[yy] + 3
    elif x=='A' and yy=='C':
        points = 0
    elif x=='B' and yy == 'A':
        points = 0
    elif x=='C' and yy =='B':
        points = 0
    else:
        points = 6
    return points + map[yy]

def rps2(play):
    x, y = play

    if y == 'Y':
        return 3 + map[x]
    if x == 'A' and y =='Z':
        return 6 + map['B']
    if x == 'A' and y=='X':
        return 0 + map['C']
    if x == 'B' and y=='Z':
        return 6 + map['C']
    if x == 'B' and y=='X':
        return 0 + map['A']
    if x== 'C' and y == 'Z':
        return 6 + map['A']
    if x == 'C' and y == 'X':
        return 0 + map['B']

print(sum([rock_paper_scissors(x) for x in plays]))

print(sum([rps2(x) for x in plays]))
