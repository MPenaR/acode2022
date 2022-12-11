class game:
    def __init__(self, you, me, second_part = False ):
        if second_part:
            self.you = parse(you)
            self.me = choose_code(you,me)
            self.score = parse_score(me)
            self.total_score = self.score + self.me 
        else:
            self.you = parse(you)
            self.me = parse(me)
            self.score = score( you, me)
            self.total_score = self.score + self.me 



def parse( code : str ) -> int :
    #Rock
    if code in [ "X", "A" ] :
        return 1 
    #Paper
    if code in [ "Y", "B" ] :
        return 2 
    #Scisors
    if code in [ "Z", "C" ] :
        return 3
    return -1



def score(you : str, me : str ) -> int :
    code = you+me
    
    #win
    if code in [ "AY", "BZ", "CX"]:
        return 6
    #draw
    if code in [ "AX", "BY", "CZ"]:
        return 3
    #loose
    if code in [ "AZ", "BX", "CY"]:
        return 0
    
    return -1



def parse_score( code : str ) -> int:
    
    #win
    if code == 'Z':
        return 6
    #draw
    if code == 'Y':
        return 3
    #loose
    if code == 'X':
        return 0
    
    return -1


def choose_code(you : str, code : str ) -> int :
    code = you+code
    
    #Rock
    if code in [ "AY", "BX", "CZ"]:
        return 1
    #Paper
    if code in [ "AZ", "BY", "CX"]:
        return 2
    #Scisors
    if code in [ "AX", "BZ", "CY"]:
        return 3
    
    return -1






with open(file='input', mode='r') as f:
    lines = f.readlines()
    games_1 = [ game( *line.rstrip().split(' ') ) for line in lines]
    games_2 = [ game( *line.rstrip().split(' '), second_part= True ) for line in lines]


print(f'Part 1: {sum( [g.total_score for g in games_1] )}')
print(f'Part 2: {sum( [g.total_score for g in games_2] )}')