def pivot(P):
    m = len(P)

    mat = [[int(i == j) for i in range(m)] for j in range(m)]

    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(P[i][j]))
        if j != row:
            mat[j], mat[row] = mat[row], mat[j]

    return mat


x = int(input("Δώσε το μήκος του πίνακα: "))
print(x)
A = [[0 for j in range(x)] for i in range(x)]
for i in range(x):
    for j in range(x):
        elements = int(input("Δώσε ένα στοιχείο του πίνακα: "))
        A[i][j] = elements

P = pivot(A)

U = [[0 for j in range(x)] for i in range(x)]
L = [[0 for j in range(x)] for i in range(x)]

sum1 = 0
sum2 = 0

for i in range(x):
    for j in range(i):
        for l in range(j):
            sum1 = sum1 + L[i][l] * U[l][j]
        L[i][j] = (A[i][j]- sum1) / U[j][j]
        sum1 = 0

    L[i][i] = 1
    j = i
    while j < x:
        for l in range(i):
            sum2 = sum2 + L[i][l] * U[l][j]
        U[i][j] = A[i][j] - sum2
        sum2 = 0
        j = j + 1

print("A= " + str(A))
print("U= " + str(U))
print("L= " + str(L))
print("P= " + str(P))

b = [0 for i in range(x)]
print("Ο πίνακας b είναι μονοδιάστατος πίνακας και έχει "+str(x)+" στοιχεία: ")
for i in range(x):
    elements = int(input("Δώσε ένα στοιχείο του πίνακα: "))
    b[i] = elements



Y = [0 for i in range(x)]
Y[0] = b[0] / L[0][0]

for i in range(1, x):
    sum3 = 0
    for j in range(0, i):
        sum3 = sum3 + L[i][j] * Y[j]
    Y[i] = (b[i]-sum3) / L[i][i]

Χ = [0 for i in range(x)]
Χ[x-1] = Y[x-1] / U[x-1][x-1]
for i in range(x - 1, -1, -1):
    sum4 = 0
    for j in range(i + 1, x):
        sum4 = sum4 + U[i][j] * Χ[j]
    Χ[i] = float(Y[i] - sum4) / U[i][i]

for i in range(x):
    print("x" + str(i+1) + "=" + str(Χ[i]))
