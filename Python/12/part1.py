import numpy as np

#def str_to_int( s : str ) -> int :


if __name__ == '__main__':
    with open(file='input', mode='r') as f:
        elevation_coded = np.array( [  list(line.rstrip()) for line in f.readlines() ] ) 
        start_position = np.argwhere(elevation_coded=='S')[0]
        end_position = np.argwhere(elevation_coded=='E')[0]
        elevation = np.array([ [ ord(s) for s in row] for row in elevation_coded ])
        elevation[start_position[0],start_position[1]] = ord('a')
        elevation[end_position[0],end_position[1]] = ord('z')
        elevation = elevation - 97
        


import matplotlib.pyplot as plt 
plt.rcParams.update({ "text.usetex": True, "font.family": "Helvetica" })
plt.imshow(elevation, interpolation='bicubic', cmap='terrain')
plt.plot(start_position[1],start_position[0], 'ok')
plt.plot(end_position[1],end_position[0], 'or')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.colorbar()
plt.show()

# import pyvista as pv 

# X, Y = np.meshgrid( np.arange(elevation.shape[1]), np.arange(elevation.shape[0]) )

# grid = pv.StructuredGrid(X, Y, elevation)
# grid.add_field_data( np.transpose(elevation), 'elevation')

# surf = grid.extract_geometry()
# grid.plot(show_edges=False, scalars="elevation", cmap='terrain') #, screenshot=f'{field_name}.png')
