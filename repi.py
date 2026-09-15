s = input()
c = 1
m = 1

for i in range(1 , len(s)):
    if s[i-1] == s[i]:
        c += 1
        if c > m :
            m = c      
    else:
        c = 1

print(m)