from pzzl import pzzl

tst = pzzl(6, True).strings()
q6 = pzzl(6, ).strings()[0]

print(tst)

def are_all_characters_unique(substr):
    return sum([substr.count(c) for c in substr]) == len(substr)

def find_unique_substring(txt, n = 4):
    # execute the subroutine on each substring
    # to find the first substring that has no repeating characters
    for i in range(n, len(txt)):
        if are_all_characters_unique(txt[i-n:i]):
            return i

for t in tst:
    print(t)
    print(find_unique_substring(t, 14))

print(find_unique_substring(q6))
print(find_unique_substring(q6, 14))

