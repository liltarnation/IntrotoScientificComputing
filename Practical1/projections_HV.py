import cv2, scipy.io

imname = 'dawg'
impath = 'Practical_Tomography/' + imname + '.png'

A = cv2.imread(impath)

white = [255, 255, 255]
rowsum = [0] * len(A)
colsum = [0] * len(A)

for i in range (len(A)):
    for j in range (len(A)):
        #computing column sums
        if ((A[j][i] == white).all()):
            colsum[i] += 1
        #computing row sums
        if ((A[i][j] == white).all()):
            rowsum[i] += 1

matlab_result = {"colsum": colsum, "rowsum": rowsum}

projfile = imname + '_HVproj' + '.mat'
scipy.io.savemat(projfile, matlab_result)