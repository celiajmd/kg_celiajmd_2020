#input the strings
s1 = input()
s2 = input()

#find out if the two strings are mapping
def ifMapping(s1: str, s2: str) -> object:
    if len(s1) != len(s2):
        return False

    d = {}
    for i in range(len(s1)):
        if s1[i] not in d:
            d[s1[i]] = s2[i]
        elif d[s1[i]] != s2[i]:
            return False
    return True

#call the function and print out the result
print(ifMapping(s1, s2))

