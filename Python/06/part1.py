def find_marker( signal : str, size_marker = 4) -> int :
    for i in range( size_marker, len(signal)):
        letters = set( signal[ i-size_marker : i ])
        if len(letters) == size_marker:
            print( '...'+signal[i-size_marker - 3:i-size_marker] + signal[i-size_marker:i].upper() + signal[i:i+3]+'...' )
            break
    return i

if __name__ == '__main__':
    with open(file='input',mode='r') as f:
        signal = f.read().rstrip()
    print('Part 1:')
    print(find_marker(signal))
    print('Part 2:')
    print(find_marker(signal, size_marker=14))