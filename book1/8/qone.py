def create_zeros_matrix(rows,cols):
    matrix=[]
    for _ in range(rows):
        row_idx=[0]*cols
        matrix.append(row_idx)
    return matrix

def identity_matrix(size):
    matrix=[]
    for i in range(size):
        row=[0]*size
        row[i]=1
        matrix.append(row)
    return matrix

def diagonal_matrix(values):
    size=len(values);matrix=[]
    for i in range(size):
        row=[0]*size
        matrix.append(row)
        matrix[i][i]=values[i]
    return matrix

def extract_main_diagonal(matrix):
    rows=len(matrix);cols=len(matrix[0])
    size=min(rows,cols)
    diagonal=[matrix[i][i] for i in range(size)]
    return diagonal

def trace(matrix):
    rows=len(matrix)
    if rows != cols:
        raise ValueError("Matrix is not square")
    diagonal_sum= sum(matrix[i][i] for i in range(rows))
    return diagonal_sum

def is_symmetric(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    #判断是否为方阵
    if rows!= cols:
        return Flase
    #判断是否对称
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_symmetric_2(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    if rows != cols:
        return False

    tranposed=[[(matrix[j][i])
                for j in range(rows)]
                for i in range(rows)]
    if(matrix == tranposed):
        return True
    return False

def determinant_2x2(matrix):
    if len(matrix)!=2 or len(matrix[0])!=2:
        raise ValueError("Mtrix must be 2x2")
    a=matrix[0][0]
    b=matrix[0][1]
    c=matrix[1][0]
    d=matrix[1][1]
    det=a*d-b*c
    return det

def inverse_2x2(matrix):
    if len(matrix)!=2 or len(matrix[0])!=2:
        raise ValueError("Matrix must be 2x2")

    a=matrix[0][0]
    b=matrix[0][1]
    c=matrix[1][0]
    d=matrix[1][1]

    det = a*d - b*c
    if det ==0:
        raise ValueError("Matrix is not invertible")

    inv_det=1/det
    inv_matrix=[[d*inv_det,-b*inv_det],
                [-c*inv_det,a*inv_det]]

    return inv_matrix









