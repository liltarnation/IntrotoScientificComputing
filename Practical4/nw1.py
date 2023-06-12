import numpy as np

file = open('nw_test1.txt') # open input file

s = file.readline() # readline 1 of the input
t = file.readline() # readline 2 of the input

file.close() # close file

lens = len(s) # length string s
lent = len(t) # length string t

p=0
q=4
g=5

D = np.zeros((lens,lent), dtype=int)
for i in range(1,lens+1):
    D[i-1,0] = (i-1)*g

for i in range(1,lent+1):
    D[0,i-1] = (i-1)*g

for i in range (1, lens):
    for j in range (1, lent):
        score = 0
        if s[i-1] == t[j-1]:
            score = p
        else:
            score = q
        Match = D[i-1,j-1] + score
        Delete = D[i-1, j] + g
        Insert = D[i, j-1] + g
        D[i,j] = min(Match, Insert, Delete)
        
print("D=", *D, sep='\n')
