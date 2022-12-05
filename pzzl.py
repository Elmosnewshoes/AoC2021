from pprint import pprint
from typing import Tuple

class pzzl:
    def __init__(self, day: int, test: bool = False, pt2 : bool = False) -> None:
        if not test:
            filename = f'input_d{str(day)}.txt'
        else:
            filename = f'tst_d{str(day)}.txt'
        if pt2:
            filename.replace('.txt' , '_pt2.txt')


        with open(filename) as f:
            self.inp = [l[:-1] for l in f]

        self.raw = [l for l in self.inp if (l != '\n' and l != '')]

    def ints(self, ) -> Tuple[int]:
        return tuple([int(x) for x in self.raw])

    def strings(self, )->Tuple[str]:
        return tuple(self.raw)

if __name__ == '__main__':
    Puzzle = pzzl(1, False)
    pprint(Puzzle.raw)
    print(Puzzle.ints())
