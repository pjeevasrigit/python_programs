
A = [[1,2,3,4],
     [3,4,5,5],
     [5,5,6,6]]

B = [[11,12,13,5],
     [3,4,5,5],
     [5,5,6,7]]

result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

for row in result:
    print(row)

