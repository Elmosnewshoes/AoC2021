import numpy as np

def to_array(txtline):
    return np.array([int(x) for x in txtline.replace('\n','').replace(' ',',').split(',') if x != ''])

class PuzzleCard:

    def __init__(self, firstline):
        self.card = firstline
        self.last_nmbr = 0
        self.done = False


    def __add__(self, other):
        self.card = np.vstack([self.card, other])
        return self


    def cross_off(self, nmbr):
        self.last_nmbr = nmbr
        self.card = np.where(self.card==nmbr, -1, self.card)


    def eval_bingo(self):
        if self.done:
            return False
        self.done = True
        chck = self.card.shape[0] * -1
        if chck in self.card.sum(axis = 0):
            return True
        if chck in self.card.sum(axis = 1):
            return True
        self.done = False
        return False

    
    def score(self):
        tmp = np.where(self.card == -1, 0, self.card).flatten()
        return tmp.sum()*self.last_nmbr

    def __str__(self,):
        return np.array2string(self.card)


def puzzle(filename):
    cards = []
    with open(filename) as f:
        draws = to_array(f.readline()) 

        for l in f:
            if l == '\n':
                cards.append(PuzzleCard(to_array(f.readline())))
            else:
                cards[-1] += to_array(l)
    return cards, draws

def play_game(cards, draws):
    scores = []
    for nmbr in draws:
        for card in cards:
            card.cross_off(nmbr)
            if card.eval_bingo():
                scores.append(card.score())


    print(f'First to win has a score of {scores[0]}')
    print(f'Last to win has a score of {scores[-1]}')


play_game(*puzzle('input_d4.txt'))
