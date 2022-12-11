with open('input', mode='r') as f:
    lines = f.readlines()

class elve_record:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item( self, val : int ):
        self.items.append(val)
        self.total += val
        return None

elve_records = [elve_record()]

for line in lines:
    if line != '\n':
        elve_records[-1].add_item(int(line))
    else:
        elve_records.append(elve_record())


elve_records = sorted(elve_records, key = lambda record : record.total, reverse=True)

print("first part")

print(elve_records[0].total)

print("second part")

print( elve_records[0].total + elve_records[1].total + elve_records[2].total )