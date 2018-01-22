txt='aasdqdagq1fafcacadabxcbaf'


txt2=txt.lower()


count=[]


for i in range(26):
    count.append(0)


start=ord('a')
for c in txt2:
    if c.isalpha():
        ix=ord(c)-start
        count[ix]=count[ix]+1

for i in range(24):
    if count[i]!=0:
        print('%c : %d:'%(chr(start+i),count[i]))