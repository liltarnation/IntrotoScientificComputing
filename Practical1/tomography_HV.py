import scipy.io, cv2, numpy as np

imname = 'rectangle'
projfile = imname + '_HVproj' + '.mat'
matlab_result = scipy.io.loadmat(projfile)

colsum = matlab_result['colsum'][0]
rowsum = matlab_result['rowsum'][0]
n = len(colsum)
MAX_ITER = 1000
eps = 0.00000005

#initialising empty matrixes
f0 = np.zeros((n,n))
fn = np.zeros((n,n))
finit = np.zeros((n,n))

# kaczmarz method for reconstruction
for k in range(MAX_ITER):
    #setting f0
    f0 = finit.copy()
    
    #looping through columns
    Bc = np.zeros(n)
    for c in range(n):
        Bc[c] = (sum(f0[:,c]) - colsum[c])/n
        fn[:,c] = f0[:,c] - Bc[c]
    #correcting for pos and neg values
    fn[fn<0]=0            
    fn[fn>1]=1  

    #setting f0
    f0 = fn
    #looping through rows
    Br = np.zeros(n)
    for r in range(n):
        Br[r] =  (sum(f0[r,:]) - rowsum[r])/n
        fn[r,:] = f0[r,:] - Br[r]
    #correcting for pos and neg values
    fn[fn<0]=0            
    fn[fn>1]=1   

    #comparing our reconstructed matrix with accuracy threshold   
    relDif = abs(np.matrix(fn).sum() - np.matrix(finit).sum() ) / (n*n)
    if (relDif < eps):
        break

    #setting finit
    finit = fn.copy()

#converting 1 values to white rgb value
np.matrix(fn).round(0,fn)
fn[fn==1]=255

#saving recreated image
recfile = imname + '_HVrec_' + '_k=' + str(k) + '_eps=' + str(eps) + '.png'
cv2.imwrite(recfile, fn)

#saving difference image
impath = 'Practical_Tomography/' + imname + '.png'
A = cv2.imread(impath)
A = A[:,:,0]
E = abs(np.matrix(fn).sum() - np.matrix(A).sum() ) / (n*n)
print(E)
dif = fn - A

diffile = imname + '_HVdif_' + '_k=' + str(k) + '_eps=' + str(eps) + '.png'
cv2.imwrite(diffile, dif)