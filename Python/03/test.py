with open(file="input", mode='r') as  f:
    lines = [ line.rstrip() for line in  f.readlines() ]


class Rucksack:
    def __init__(self, code : str):
        self.LeftCompartment = set(code[:len(code)//2])
        self.RightCompartment = set(code[len(code)//2:])
    
    def common_item(self) -> str :
        return list( self.LeftCompartment & self.RightCompartment )[0] 
    
Rucksacks = [ Rucksack(line) for line in lines ]


def priority(l : str) -> int :
    if is_upper(l):
        return ord(l) - 65 + 27
    if is_lower(l):
        return ord(l) - 97 + 1
    return -1

def is_upper( l : str ) -> bool :
    return l.upper() == l 

def is_lower( l : str ) -> bool :
    return l.lower() == l 

print( sum( [ priority( r.common_item()) for r in Rucksacks ] ) )
