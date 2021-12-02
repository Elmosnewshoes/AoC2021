from pzzl import pzzl

inp = pzzl(2, False)

class sub:
    def __init__(self, lat, depth):
        self.y = lat
        self.h = depth
        self.aim = 0

    def move(self, command):
        mve, quant = command.split(' ', 1)
        if mve == 'down':
            self.h += int(quant)
        elif mve == 'up':
            self.h -= int(quant)
        elif mve == 'forward':
            self.y += int(quant)
        else:
            self.y -= int(quant)
        return mve, quant

    def move2(self, command):
        mve, quant = command.split(' ', 1)
        if mve == 'down':
            self.aim += int(quant)
        if mve == 'up':
            self.aim -= int(quant)
        if mve == 'forward':
            self.y += int(quant)
            self.h += int(quant)*self.aim


    def ans1(self):
        print(f'Boat is at pos {self.y}, depth {self.h} -> {self.y * self.h}')

uboot = sub(0,0)
for command in inp.strings():
    uboot.move(command)

uboot.ans1()

uboot = sub(0,0)
for command in inp.strings():
    uboot.move2(command)

uboot.ans1()
