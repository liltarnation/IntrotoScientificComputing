import scipy.io, cv2, numpy as np

imname = 'rock'
projfile = imname + '_HVproj' + '.mat'
matlab_result = scipy.io.loadmat(projfile)

colsum = matlab_result['colsum'][0]
rowsum = matlab_result['rowsum'][0]
n = len(colsum)
MAX_ITER = 150
eps = 0.000001
f0 = []
fn = []
finit = []

#initialising empty matrixes
for i in range (n):
    f0.append([0]*n)
    fn.append([0]*n)
    finit.append([0]*n)

#kaczmarz method for reconstruction
for k in range(MAX_ITER):
    #setting f0
    f0 = finit
    #looping through columns
    Bc = [0]*n
    for c in range(n):
        sum = 0
        for x in range(n):
            sum += f0[x][c]
        Bc[c] = (sum - colsum[c])/n
        for x in range(n):
            fn[x][c] = f0[x][c]-Bc[c]
    #updating min max    
    for i in range(n):
        for y in range(n):
            fn[i][y]= min(max(fn[i][y],0),1)

    #setting f0
    f0 = fn
    #looping through rows
    Br = [0]*n
    for r in range(n):
        sum = 0
        for x in range(n):
            sum += f0[r][x]
        Br[r] =  (sum - rowsum[r])/n
        for x in range (n):
            fn[r][x] = f0[r][x]-Br[r]
    #updating min max   
    for i in range(n):
        for y in range(n):
            fn[i][y]= min(max(fn[i][y],0),1)

    # implenting epsilon beak thing
    sumFn = 0
    sumFinit = 0
    for x in range (n):
        sumFn += np.sum(fn[:][x])
        sumFinit += np.sum(finit[:][x])
    E = abs(sumFn - sumFinit)/(n*n)
    
    if (E < eps):
        break

    #setting finit
    finit = fn

#converting 1 values to white rgb value
for i in range(n):
    for y in range(n):
        fn[i][y]= round(fn[i][y])
        if (fn[i][y] == 1):
            fn[i][y] = 255

recfile = imname + '_HVrec_' + '.png'
cv2.imwrite(recfile, np.array(fn))