import numpy as np
class crane():
    def __init__( self, code : list):
        len_lines = max( [ len(line) for line in code ])
        code = [ line.ljust(len_lines)  for line in code ]
        self.N_stacks = 9
        code_grid = np.array( [ list(line) for line in code ]).reshape((8,-1))
   
        self.stacks = []
        for i in range(1,self.N_stacks*4,4):
            self.stacks.append(list(''.join(code_grid[:,i]).lstrip()))

    def move( self, origin : int, destiny : int, n_boxes : int, part_one = False) :

        boxes = self.stacks[origin][:n_boxes]
        self.stacks[origin] = self.stacks[origin][n_boxes:]
        if part_one :
            self.stacks[destiny] = boxes[::-1] + self.stacks[destiny]
        else:
            self.stacks[destiny] = boxes + self.stacks[destiny]
        return

        # for _ in range(n_boxes):
        #     self.single_move( origin=origin, destiny=destiny)

    def print( self ):
        for i in range(self.N_stacks):
            print(self.stacks[i])



# def box_parser

def command_parser( line : str ):
    words = line.split(' ')
    #print(f'from {} to {} move {int}')
    return ( int(words[3])-1, int(words[5])-1, int(words[1]))



if __name__ == '__main__':
    with open( file='input', mode='r' ) as f:
        lines = [ line.rstrip() for line in f.readlines()]

    boxes = lines[:8]
    commands = lines[10:]

    S = crane(boxes)
    S.print()
    print('=======')
    for command in commands:
        S.move( *command_parser(command), part_one=False)
    print(''.join( [ s[0] for s in S.stacks]))