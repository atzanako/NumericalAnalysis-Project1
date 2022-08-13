import numpy as np
import math

def cholesky(A):
    L = np.zeros(A.shape, dtype=float)
    for u in range(0, L.shape[0]):
        for h in range(0, u):
            sum_col = 0

            for w in range(0, u):
                sum_col = sum_col + L[u][w] * L[h][w]
            L[u][h] = (A[u][h] - sum_col) / L[h][h]

        sum_col = 0

        for w in range(0, u):
            sum_col = sum_col + math.pow(L[u][w], 2)
        L[u][u] = math.sqrt(A[u][u] - sum_col)

    return L


def gauss_seidel(A, x, b, n):
    for i in range(0, n):
        w = b[i]
        for j in range(n):
            if i != j:
                w = w - (A[i][j] * x[j])
        x[i] = w/A[i][i]
    return x


n = int(input("Δώσε τον αριθμό των αγνώστων: "))
A = [[0 for j in range(n)] for i in range(n)]
x = [0 for j in range(n)]

A[n-1][n-1] = 5
A[n-1][n-2] = -2
A[0][0] = 5
A[0][1] = -2

for i in range(1, n-1):
    A[i][i] = 5
    A[i][i+1] = -2
    A[i][i-1] = -2

print(A)
b = [1 for j in range(0, n)]
b[0] = 3
b[n-1] = 3
print(b)
for i in range(0, n):
    x = gauss_seidel(A, x, b, n)
    print(x)

for i in range(0, n):
    x[i] = round(x[i])

print("Η λύση του συστήματος με την μέθοδο Gauss-Seidel είναι η εξής: "+str(x))