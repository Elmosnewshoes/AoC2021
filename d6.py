from pzzl import pzzl

tst = pzzl(6, True).strings()
q6 = pzzl(6, ).strings()[0]

print(tst)

def are_all_characters_unique(txt, i = 0):
    # ugly recursive function
    # start at the first char of the substring
    # if it is unique in the whole substring
    # execute this function for the next char in the substring
    # until the substring is exhausted, then return True
    # if a character is not unique in the substring, return False
    if i == len(txt):
        # reached last element, search for char in substr complete
        return True
    subj = txt[i]
    if txt.count(subj) > 1:
        return False
    else:
        return are_all_characters_unique(txt, i+1)

def find_unique_substring(txt, n = 4):
    # execute the subroutine to on each substring
    # to find the first that hass no repeating characters
    for i in range(n, len(txt)):
        if are_all_characters_unique(txt[i-n:i], 0 ):
            return i

for t in tst:
    print(t)
    print(find_unique_substring(t, 14))

print(find_unique_substring(q6))
print(find_unique_substring(q6, 14))

