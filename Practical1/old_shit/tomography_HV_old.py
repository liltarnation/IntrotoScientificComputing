from platform import machine
import scipy.io
import cv2
import numpy as np

imname = 'oval'
projfile = imname + '_HVproj' + '.mat'
matlab_result = scipy.io.loadmat(projfile)

colsum = matlab_result['colsum'][0]
rowsum = matlab_result['rowsum'][0]

n = len(matlab_result['colsum'][0])

MAX_ITER = 150
eps = 0.000001

f0 = []
fn = []
finit = []

for i in range (n):
    f0.append([0]*n)
    fn.append([0]*n)
    finit.append([0]*n)

for k in range(MAX_ITER):
    #setting f0
    for i in range(n):
        for y in range(n):
            f0[i][y] = finit[i][y]

    #looping through colums
    temp = [0]*n
    Bc = [0]*n
    for c in range(n):
        for x in range(n):
            temp[c] += f0[x][c]
        Bc[c] = (temp[c] - colsum[c])/n
        for x in range(n):
            fn[x][c] = f0[x][c]-Bc[c]

    for i in range(n):
        for y in range(n):
            fn[i][y]= min(max(fn[i][y],0),1)

    #reset f0
    for i in range(n):
        for y in range(n):
            f0[i][y]= fn[i][y]

    #looping through rows
    Bc = [0]*n
    temp = [0]*n

    for r in range(n):
        for x in range(n):
            temp[r] += f0[r][x]
        Bc[r] =  (temp[r] - rowsum[r])/n
        
    for i in range(n):
        for y in range(n):
            fn[i][y]= min(max(fn[i][y],0),1)

    # implent epsilon beak thing

    #resetting finit
    for i in range(n):
        for y in range(n):
            finit[i][y]= fn[i][y]

for i in range(n):
    for y in range(n):
        fn[i][y]= round(fn[i][y])
        if (fn[i][y] == 1):
            fn[i][y] = 255
for i in fn:
    print(i)


recfile = imname + '_HVrec_' + '.png'
cv2.imwrite(recfile, np.array(fn))