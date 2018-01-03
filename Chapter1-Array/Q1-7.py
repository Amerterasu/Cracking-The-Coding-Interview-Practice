def rotateMatrix(matrix, N):
    if N % 2 != 0:
        layers = int((N-1)/2)
    else:
        layers = int(N/2)
    
    for layer in range(layers):
        for pixel in range(layer, N-1-layer):
            tmp = matrix[layer][pixel]
            tmp2 = matrix[pixel][N-1-layer]
            tmp3 = matrix[N-1-layer][N-1-layer-pixel]
            tmp4 = matrix[N-1-layer-pixel][layer]
            
            matrix[layer][pixel] = tmp4
            matrix[pixel][N-1-layer] = tmp
            matrix[N-1-layer][N-1-pixel] = tmp2
            matrix[N-1-layer-pixel][layer] = tmp3
    
    return matrix

print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]], 3))
print(rotateMatrix([[1,2],[3,4]], 2))