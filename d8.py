from pzzl import pzzl

def output_to_number(segm):
    if len(segm)== 2:
        return 1
    if len(segm) == 4:
        return 4
    if len(segm) == 3:
        return 7
    if len(segm) == 7:
        return 8
    return -1

def parse_signal(signal):
    signal_pattern, digit_output = signal.split(' | ', 1)
    counter = 0
    for segm in digit_output.split(' '):
        if output_to_number(segm) > -1:
            counter += 1
    return counter


signals = pzzl(8, False).strings()
counter = 0
for rw in signals:
    counter += parse_signal(rw)

print(counter)

def combine(*inputs):
    inp = ''
    for i in inputs:
        inp += i
    return ''.join(list((set([lttr for lttr in inp]))))

def reduce_str(a: str, b: str) -> str:
    return ''.join([ch for ch in a if ch not in b])

def inp_reduce(tgt, *inputs):
    return reduce_str(tgt, ''.join(inputs))

class Digit:
    def __init__(self, inp):
        signal_line, output_line = inp.split(' | ')
        self.signals = signal_line.split(' ')
        self.output = output_line.split(' ')
        self.digits = ['' for _ in range(10)]

    def d(self, ind):
        return self.digits[ind]

    def len_reduce(self, x, *indexes):
        return len(inp_reduce(x, *[self.d(i) for i in indexes]))

    def map_knowns(self):
        for signal in self.signals:
            if (ind := output_to_number(signal)) > -1:
                self.digits[ind] = signal
        while len([s for s in self.digits if s == '']) > 1:
            for signal in [x for x in self.signals if x not in self.digits]:
                if (len(signal) == 6 and self.len_reduce(signal, 4, 7) == 1):
                    self.digits[9] = signal
                elif (len(signal) == 5 and self.len_reduce(signal, 9) == 1):
                    self.digits[2] = signal
                elif (len(signal) == 5 and self.len_reduce(signal, 2) == 1):
                    self.digits[3] = signal
                elif(len(signal) == 5 and self.len_reduce(signal, 9) == 0):
                    self.digits[5] = signal
                elif(len(signal) == 6 and self.len_reduce(signal, 3, 2) ==
                     1 and self.len_reduce(signal, 7) == 4):
                    self.digits[6] = signal

        for s in self.signals:
            if s not in self.digits:
                self.digits[0] = s

    def print_digit(self, digit):
        def sorted_digit(x):
            return ''.join(sorted(x))

        for i, d in enumerate(self.digits):
            if sorted_digit(d) == sorted_digit(digit):
                return str(i)

    def digit_sum(self):
        return int(''.join([self.print_digit(x) for x in self.output]))




counter = 0
for ln in signals:
    d = Digit(ln)
    d.map_knowns()
    counter += d.digit_sum()
    print(d.output, d.digit_sum())

print(counter)
