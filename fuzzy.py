A = {
    "a":1.0,
    "b":0.6,
    "c":0.9,
}

B = {
    "a":1.0,
    "b":0.6,
    "c":0.3,
}
Y=dict()
 
for k1, k2 in zip(A, B):
    v1 = A[k1]
    v2 = B[k2]

    if v1 > v2:
        Y[k1] = v1
    else:
        Y[k2] = v2
print('Union:', Y)
        
