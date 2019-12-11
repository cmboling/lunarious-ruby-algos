N = 1000

def rotateOldMatrix(oldMatrix): 
    for x in range(int(N/2)): 
        for y in range(x, N-x-1): 
              
            # store temp 
            temp = oldMatrix[x][y] 
  
            # right to top 
            oldMatrix[x][y] = oldMatrix[y][N-1-x] 
  
            # bottom to right 
            oldMatrix[y][N-1-x] = oldMatrix[N-1-x][N-1-y] 
  
            # left to bottom 
            oldMatrix[N-1-x][N-1-y] = oldMatrix[N-1-y][x] 
  
            # assign temp
            oldMatrix[N-1-y][x] = temp 
