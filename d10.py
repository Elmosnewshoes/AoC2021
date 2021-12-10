from pzzl import pzzl

matching_brackets = {
    '[': ']',
    '{': '}',
    '(': ')',
    '<': '>'
}

scores = dict(zip(matching_brackets.values(), [57, 1197, 3, 25137]))
scores2 = dict(zip(matching_brackets.values(), [2, 3, 1, 4]))


def find_wrong_bracket(line):
    brackets = [line[0]]
    for ch in line[1:]:
        if ch in matching_brackets.keys():
            brackets.append(ch)
        elif ch != matching_brackets[brackets[-1]]:
            return scores[ch], []
        else:
            brackets = brackets[:-1]
    return 0, brackets

def closing_to_score(closing):
    closing.reverse()
    score = 0
    for ch in closing:
        score *= 5
        score += scores2[matching_brackets[ch]]
    return score

inp = pzzl(10, False).strings()
score = 0
for rw in inp:
    score += find_wrong_bracket(rw)[0]

print(f'Pt 1: {score}')

score_list = []
for rw in inp:
    x, closing = find_wrong_bracket(rw)
    if x == 0:
        score_list.append(closing_to_score(closing))
score_list = sorted(score_list)

print(score_list[int(len(score_list)/2)])
