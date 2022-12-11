import numpy as np
from functools import reduce
if __name__ == '__main__': 

    with open(file='input', mode='r') as f:
        grid = np.array( [ list(line.rstrip()) for line in f.readlines() ] ).astype('int')


    M, N = grid.shape

    #top
    top = np.zeros_like(grid, dtype=bool)
    top[0,:] = True
    val = grid[0,:]
    for i in range(1,M):
        top[i,:] = grid[i,:] > val
        val = np.where( grid[i,:] > val, grid[i,:], val)
    
    #left
    left = np.zeros_like(grid, dtype=bool)
    left[:,0] = True
    val = grid[:,0]
    for j in range(1,N):
        left[:,j] = grid[:,j] > val
        val = np.where( grid[:,j] > val, grid[:,j], val)

    #right
    right = np.zeros_like(grid, dtype=bool)
    right[:,-1] = True
    val = grid[:,-1]
    for j in range(N-2,-1,-1):
        right[:,j] = grid[:,j] > val
        val = np.where( grid[:,j] > val, grid[:,j], val)

    #bottom
    bottom = np.zeros_like(grid, dtype=bool)
    bottom[-1,:] = True
    val = grid[-1,:]
    for i in range(M-2,-1,-1):
        bottom[i,:] = grid[i,:] > val
        val = np.where( grid[i,:] > val, grid[i,:], val)

    viewed = reduce( lambda A, B : np.logical_or(A,B), [top, bottom, left, right], np.zeros_like(grid,dtype=bool))
    N_viewed = np.count_nonzero(viewed)
    
    # plotting
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(nrows =2, ncols=3)
    ax[0,0].imshow(grid, interpolation='bicubic')
    ax[0,1].imshow(top)
    ax[0,2].imshow(left)
    ax[1,0].imshow(bottom)
    ax[1,1].imshow(right)
    ax[1,2].imshow(viewed)
    
    ax[0,0].set_title('Tree heights')
    ax[0,1].set_title('View from top')
    ax[0,2].set_title('View from left')
    ax[1,0].set_title('View from bottom')
    ax[1,1].set_title('View from right')
    ax[1,2].set_title(f'Viewed trees: {N_viewed}')

    plt.show()
    