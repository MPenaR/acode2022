max_size = 100000

total_space  = 70000000
needed_space = 30000000

class FileSystem:
    def __init__(self):
        self.root = Directory('') # adding the root directory
        self.pwd = self.root      # initializing the working directory

    def cd( self, name : str):
        '''Emulates the behaviour of `cd` '''
        if name == '/':
            self.pwd = self.root
        elif name == '..':
            self.pwd = self.pwd.parent
        else:
            self.pwd = self.pwd.subdirectories[name]
    def mkdir( self, name):
        '''Emulates the behaviour of `mkdir` '''
        pwd = self.pwd
        pwd.add_subdirectory(name)

    def ls(self):
        '''Emulates the behaviour of `ls` '''
        for dir in self.pwd.subdirectories:
            print(f'{dir} (dir)')
        for fname, f in self.pwd.files.items():
            print(f'{fname} (file, size={f.size})')
    
    def __str__(self):
        representation = ''
        dl = 0
        def recursive_repr(repr: str, dl, dir):
            dl = dl+1
            tabs = dl*'\t'            
            for (name, subdir) in dir.subdirectories.items():
                repr = repr + f"{tabs}- {name} (dir, size = {subdir.size}) \n"
                repr, dl = recursive_repr(repr, dl, subdir)
            for (name, f) in dir.files.items():
                repr = repr + f"{tabs}- {name} (file, size={f.size}) \n"
            dl = dl - 1
            return repr, dl
        
        representation = representation + f'- / (dir, size = {self.root.size}) \n'
        representation, dl = recursive_repr(representation, dl, self.root)
        return representation
    def compute_sizes( self ):
        self.root.compute_sizes()
        return

    def dir_sizes(self):
        sizes = []

        def append_sizes(dir, sizes):
            for subdir in dir.subdirectories.values():
                append_sizes(subdir, sizes)
                sizes.append(subdir.size)
        
        append_sizes(self.root, sizes)
        sizes.append(self.root.size)

        return sizes
  
class Directory: 
    def __init__(self, name : str, parent=None):
        self.parent = parent
        if parent is not None:
            self.route = "/".join([parent.route, name] )
        else:
            self.route = ''
        self.files = dict()
        self.subdirectories = dict()
        self.size = 0
    
    def add_file(self, file_name : str, file_size: int):
        self.files[ file_name] = File( file_name = file_name, file_size= file_size)
    
    def add_subdirectory( self, name ):
        d = Directory( name=name, parent = self)
        self.subdirectories[ name ] = d
        return d
    
    def compute_sizes( self ):
        for subdir in self.subdirectories.values():
            subdir.compute_sizes()
        self.size = self.size + sum([subdir.size for subdir in self.subdirectories.values()])
        self.size = self.size + sum([f.size for f in self.files.values()])
        return
        
    def __str__(self):
        return self.route+'/'

class File:
    def __init__(self, file_name : str, file_size : int ):
        self.name = file_name
        self.size = file_size


def parse_lines(lines, FS):
    for line in lines:
        words = line.split(' ')
        if words[0] == '$': #is command
            if words[1] == 'ls':
                pass
            else:
                FS.cd(words[2])
        else:
            if words[0] == 'dir':
                FS.mkdir(name=words[1])
            else:

                FS.pwd.add_file( file_name = words[1], file_size = int(words[0]))
    return FS






if __name__ == '__main__':
    with open(file='input', mode='r') as f:
        lines = [line.rstrip() for line in  f.readlines()]

    FS = FileSystem() 
    FS = parse_lines(lines, FS)

    FS.compute_sizes()
    print(FS)

    sizes = FS.dir_sizes()

    print('part 1:')

    print(sum([size for size in sizes if size < max_size ]))
    sizes = sorted(sizes)
    used_space = sizes[-1]
    free_space = total_space - used_space
    space_to_del = needed_space - free_space
    
    print('part 2:')
    for size in sizes:
        if size > space_to_del:
            print(size)
            break