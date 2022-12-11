class zone_range:
    def __init__(self, code : str ):
        a, b = code.split('-')
        self.zones = set(range(int(a), int(b)+1))
    
    def overlap(self, other ) -> bool :
        return len( self.zones & other.zones ) > 0

if __name__ == '__main__':
    with open( file = 'input', mode = 'r') as f:
        lines = [ line.rstrip() for line in f.readlines()]
    
    zones = [ [ zone_range( line.split(',')[0]), zone_range( line.split(',')[1]) ] for line in lines ]

    print('Part 1:')
    print( sum( [ int( z[0].zones.issubset(z[1].zones) or z[1].zones.issubset(z[0].zones) ) for z in zones]))
    print('Part 2:')
    print( sum( [ int( z[0].overlap(z[1]) ) for z in zones]))
    