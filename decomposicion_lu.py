import scipy
import scipy.linalg

matriz=[[1, 2], [2, 1]]
print('2x2')
nueva_matriz = scipy.linalg.lu(matriz)
print(nueva_matriz)

matrix=[[1, -2, -2, -3], [3, -9, 0, -9], [-1, 2, 4, 7], [-3, -6, 26, 2]]
print('4x4')
new_matrix = scipy.linalg.lu(matrix)
print(new_matrix)
print('inverse_4x4')
new_inverse_matrix = scipy.linalg.inv(matrix)
print(new_inverse_matrix)

