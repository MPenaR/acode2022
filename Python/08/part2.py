import numpy as np
from functools import reduce

if __name__ == '__main__': 

    with open(file='input', mode='r') as f:
        grid = np.array( [ list(line.rstrip()) for line in f.readlines() ] ).astype('int')

    M, N = grid.shape

    down = np.zeros_like(grid)
    ind = np.ones_like(grid,dtype=bool)
    ind[-1, : ] = False
    down[ind] = 1
    for i in range(1,M-1):
        ind = np.concatenate( [ np.logical_and( ind[0:-(i+1),:], grid[0:-(i+1),:] > grid[i:-1,:] ),
                                np.zeros( [(i+1),N], dtype=bool)],
                                axis=0 )
        down[ind] += 1

    right = np.zeros_like(grid)
    ind = np.ones_like(grid,dtype=bool)
    ind[ :, -1 ] = False
    right[ind] = 1
    for j in range(1,N-1):
        ind = np.concatenate( [ np.logical_and( ind[:,0:-(j+1)], grid[:,0:-(j+1)] > grid[:,j:-1] ),
                                np.zeros( [M,(j+1)],
                                dtype=bool)], axis=1 )
        right[ind] += 1

    up = np.zeros_like(grid)
    ind = np.ones_like(grid,dtype=bool)
    ind[0, : ] = False
    up[ind] = 1
    for i in range(1,M-1):
        ind = np.concatenate( [ np.zeros( [(i+1),N], dtype=bool),
                                np.logical_and( ind[i+1:,:], grid[i+1:,:] > grid[1:-i,:] )],
                                axis=0 )
        up[ind] += 1

    left = np.zeros_like(grid)
    ind = np.ones_like(grid,dtype=bool)
    ind[:, 0 ] = False
    left[ind] = 1
    for j in range(1,N-1):
        ind = np.concatenate( [ np.zeros( [M, (j+1)], dtype=bool),
                                np.logical_and( ind[:,j+1:], grid[:,j+1:] > grid[:,1:-j] )],
                                axis=1 )
        left[ind] += 1

    score = down*right*up*left

    # plotting:
    import matplotlib.pyplot as plt 
    import matplotlib.colors as colors
    fig, ax = plt.subplots(nrows =2, ncols=3)
    ax[0,0].imshow(grid, interpolation='bicubic')
    ax[0,1].imshow(down)
    ax[0,2].imshow(left)
    ax[1,0].imshow(up)
    ax[1,1].imshow(right)
    ax[1,2].imshow(score, norm=colors.LogNorm())
    
    ax[0,0].set_title('Tree heights')
    ax[0,1].set_title(f'looking down, max: {np.max(down)}')
    ax[0,2].set_title(f'looking left, max: {np.max(left)}')
    ax[1,0].set_title(f'looking up, max: {np.max(up)}')
    ax[1,1].set_title(f'looking right, max: {np.max(right)}')
    ax[1,2].set_title(f'All directions, max: {np.max(score)}')

    plt.show()
    