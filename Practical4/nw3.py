import numpy as np
output = open('nw3-output.txt', 'w') # open file
output.write("Name: Dominic Therattil & Sebastian Preststulen ") # enter your name(s)
output.write("IBC, Practical 3 \n")

file = open('nw_test1.txt') # open input file
s = file.readline() # readline 1 of the input
t = file.readline() # readline 2 of the input
file.close() # close file
lens = len(s) # length string s
lent = len(t) # length string t

output.write("\n\nString s: \n")
for i in range(lens):
    output.write(s[i])  
output.write("\n\nString t: \n")
for i in range(lent):
    output.write(t[i])

#MATRIX D
output.write("\n\nMatrix D: \n")
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
for r in D:
    output.write(str(r).strip("[]")+"\n")

#MATRIX P
output.write("\n\nMatrix P: \n")
P = np.empty([lens, lent], dtype=str)
for i in range (0, lens):
    for j in range (0, lent):
        score = 0
        if s[i-1] == t[j-1]:
            score = p
        else:
            score = q
                    
        if D[i,j] == 0:
            P[i,j] = "*"
        elif D[i,j] == D[i-1,j-1] + score:
            P[i,j] = "\\"
        elif D[i,j] == D[i, j-1] + g:
            P[i,j] = "-"
        else:
            P[i,j] = "|"  
for r in P:
    output.write(''.join(r)+"\n")

#Arr Alignment
output.write("\n\nAlignment: \n")
t_al = np.empty([lens], dtype=str)
l_al = np.empty([lens], dtype=str)
j= lent-1;
for i in range(lens-1, -1, -1):
    if P[i,j] == "\\":
        j-=1
        l_al[i] = "|"
        t_al[i] = s[i-1]
    elif P[i,j] == "|":
        l_al[i] = " "
        t_al[i] = "-"   
s_al = s[0:lens-1]   
for r in s_al:
    output.write(r)
output.write("\n")
for r in l_al:
    output.write(r)
output.write("\n")
for r in t_al:
    output.write(r)

output.close() # close file