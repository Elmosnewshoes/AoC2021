from pzzl import pzzl

tst = pzzl(7, True).strings()
inp = pzzl(7, ).strings()

SIZES = []


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'{self.name} = {self.size}'

class Dir:

    def __init__(self, name, parent):
        self.name = name

        self.children = []
        self.parent = parent
        self.files = []
        self.size = None

    def get_children_sizes(self, threshold = 100000):
        return 

    def go_deep(self):
        if self.children:
            offspring = self.children
            for child in self.children:
                offspring += child.go_deep()
        else:
            return []
        return offspring

    def get_root(self):
        if self.parent:
            return self.parent.get_root()
        else:
            return self


    def get_child_by_name(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def get_size(self):
        global SIZES
        if self.size:
            return self.size
        files = [f.size for f in self.files]
        folders = [child.get_size() for child in self.children]
        self.size = sum(files) + sum(folders)
        SIZES.append(self.size)
        return self.size


    def add_child(self, term_lines):
        a, b = term_lines.split(' ')
        if a.isnumeric():
            self.files.append(File(b, int(a)))
        else:
            self.children.append(Dir(b, self))


def parse_dir(lines, current_dir):
    for line in lines:
        dir_dict = current_dir.add_child(line)
    return dir_dict


def loop_terminal(lines):
    ls = []
    current_dir = Dir('/', None)
    for l in lines[1:]:
        if l[0] != '$':
            ls.append(l)
            continue
        elif len(ls) > 0:
            parse_dir(ls, current_dir)
            ls = []
        cmd = l.replace('$ ','')
        if cmd == 'ls':
            continue
        
        instr, dir_name = cmd.split(' ')
        if dir_name == '..':
            current_dir = current_dir.parent
        else:
            current_dir = current_dir.get_child_by_name(dir_name)

    if len(ls) > 0:
        parse_dir(ls, current_dir)
    return current_dir.get_root()

root = loop_terminal(tst,)


root.get_size()
print(sum([x for x in SIZES if x <= 100000]))

SIZES.sort()

req_space = 30000000
av_space = 70000000 - root.get_size()


for x in SIZES:
    if x + av_space >= req_space:
        print(x)
        break

