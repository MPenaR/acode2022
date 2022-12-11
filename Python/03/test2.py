import numpy as np
from functools import reduce

class Elf:
    def __init__(self, code : str):
        self.Rucksack = set(code)

class Team:
    def __init__(self, codes):
        self.elves = [ Elf(code) for code in codes ]
    def badge(self):
        common = reduce( lambda a, b : a & b , [ elf.Rucksack for elf in self.elves ] )
        return list(common)[0]

def priority(l : str) -> int :
    if l.isupper():
        return ord(l) - 65 + 27
    if l.islower():
        return ord(l) - 97 + 1
    return -1


if __name__ == "__main__":

    with open(file="input", mode='r') as  f:
        lines = [ line.rstrip() for line in  f.readlines() ]

    Elfs_per_team = 3
    teams = [ Team(codes) for codes in np.array(lines).reshape((-1,Elfs_per_team)) ]

    print( sum( [ priority( t.badge()) for t in teams ] ) )

