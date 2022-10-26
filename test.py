import numpy as np

# eigenvectors and eigenvalues
A = np.array([[1, -1], [2, 4]])
# print(A)
evalues, evectors = np.linalg.eig(A)
# print(evectors)

evectors = np.transpose(evectors) # we need to transpose the matrix to get the eigenvectors
for i in range(len(evalues)):
    print('A x:', np.dot(A, evectors[ i]))
    print('lambda x:', np.dot(evalues[ i],evectors[ i]))