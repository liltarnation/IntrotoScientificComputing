import scipy.io, cv2, numpy as np

test = [[-1,2,-1],
        [-1,0.123,-1],
        [-1,2,-1]]
test = np.array(test)
test[test<0] = 0
test[test>1] = 1
# print(test[:,:])
# print(max(fn[:,:].all(),0))
# print(test[:,:])
# print(np.matrix(test).max(0).min(1))
# test[:,0] = np.matrix(test).max(0).min(1)
# for i in test:
#     print(i)
# print(sum(test[:,0]))
# print(test[0,:])
# print(np.matrix(test).sum())