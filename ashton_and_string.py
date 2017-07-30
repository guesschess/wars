# passed the first four tests. Suggestions are welcomed:)

def ashton(s, p):
    substrings = set()
    for i in range(len(s)):
        for j in range(1,len(s)-i+1):
            substrings.add(s[i:i+j])
    sort = "".join(sorted(substrings)) 
    return sort[p-1]

t = input()
for i in range(t):
    s = raw_input()
    p = input()
    print ashton(s,p)
