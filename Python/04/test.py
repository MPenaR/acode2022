import numpy as np

# class range:
#     def __init__(self, a, b):
#         self.min = a
#         self.max = b


if __name__ == '__main__':
    with open( file = 'input', mode = 'r') as f:
        lines = [ line.rstrip() for line in f.readlines()]
    
    N_lines = len(lines)

    a_min = np.array( [ line.split(',')[0].split('-')[0] for line in lines ] ).astype('int')
    a_max = np.array( [ line.split(',')[0].split('-')[1] for line in lines ] ).astype('int')
    b_min = np.array( [ line.split(',')[1].split('-')[0] for line in lines ] ).astype('int')
    b_max = np.array( [ line.split(',')[1].split('-')[1] for line in lines ] ).astype('int')
    

    
    
    uno_en_dos = np.logical_and( a_min <= b_min  , a_max >= b_max)
    dos_en_uno = np.logical_and( b_min <= a_min  , b_max >= a_max)
    contenidos = np.logical_or(  uno_en_dos, dos_en_uno )
    for i in range(4):
        print(f'{a_min[i]} {a_max[i]} {b_min[i]} {b_max[i]}')
        print(uno_en_dos[i])
        print(dos_en_uno[i])        
        print(contenidos[i])


    print( np.count_nonzero(contenidos) )

    