from pzzl import pzzl

tst = pzzl(6, True).strings()
q6 = pzzl(6, ).strings()[0]

print(tst)

def are_different(txt, i = 0):
    # ugly recursive function
    # start at the first char of the substring
    # if it is unique in the whole substring
    # execute this function for the next char in the substring
    # until the substring is exhausted, then return True
    # if a character is not unique in the substring, return False
    if i == len(txt):
        return True
    subj = txt[i]
    char_match = [ 1 for ch in txt if ch == subj ]
    if sum(char_match) > 1:
        return False
    else:
        return are_different(txt, i+1)

def find_four_different_characters(txt, n = 4):
    # execute the subroutine to on each substring
    # to find the first that hass no repeating characters
    for i in range(n, len(txt)):
        if are_different(txt[i-n:i], 0 ):
            return i

for t in tst:
    print(t)
    print(find_four_different_characters(t, 14))

print(find_four_different_characters(q6))
print(find_four_different_characters(q6, 14))

