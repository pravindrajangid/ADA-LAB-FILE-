
from typing import List

def strassen_multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Divide Matrix A into 4 parts
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    # Divide Matrix B into 4 parts
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Addition function
    def add(X, Y):
        return [
            [X[i][j] + Y[i][j] for j in range(len(X))]
            for i in range(len(X))
        ]

    # Subtraction function
    def sub(X, Y):
        return [
            [X[i][j] - Y[i][j] for j in range(len(X))]
            for i in range(len(X))
        ]

    # Calculate the 7 products
    M1 = strassen_multiply(add(A11, A22), add(B11, B22))
    M2 = strassen_multiply(add(A21, A22), B11)
    M3 = strassen_multiply(A11, sub(B12, B22))
    M4 = strassen_multiply(A22, sub(B21, B11))
    M5 = strassen_multiply(add(A11, A12), B22)
    M6 = strassen_multiply(sub(A21, A11), add(B11, B12))
    M7 = strassen_multiply(sub(A12, A22), add(B21, B22))

    # Calculate the four parts of result matrix
    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)

    # Combine the four parts
    C = []

    for i in range(mid):
        C.append(C11[i] + C12[i])

    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


# Input
n = int(input("Enter size of matrix: "))

print("Enter Matrix A:")
A = []

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter Matrix B:")
B = []

for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

# Multiplication
result = strassen_multiply(A, B)

# Output
print("Resultant Matrix:")
for row in result:
    print(*row)
