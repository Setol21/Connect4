import numpy as np
class Connect4():
    def __init__(self):
        self.table=np.zeros((7,6),dtype=np.int8)
        self.player=1
        self.keep_playing=True
        self.winner=0
    
    def change_player(self):
        if self.player==1:
            self.player=2
        else:
            self.player=1

    def check(self):
        if (4 in np.count_nonzero(self.table==self.player,axis=1)) or \
            (4 in np.count_nonzero(self.table==self.player,axis=0)):
            self.keep_playing=False
            self.winner=self.player
        else:
            # for i in range(3,)
            pass
    
    def play(self, col_place):
        if self.keep_playing==False:
            return (f'Player {self.winner} wins!')
        elif (0 not in self.table[col_place]):
            return "Column Full!"
        else:
            while True:
                for i in range(len(self.table[col_place])):
                    try:
                        if self.table[col_place][i+1]==1 or self.table[col_place][i+1]==2:
                            self.table[col_place][i]=self.player
                            self.check()
                            self.change_player()
                            return 
                    except IndexError:
                        self.table[col_place][i]=self.player
                        self.check()
                        self.change_player()
                        return 
    def show(self):
        print(self.table.T)

game=Connect4()
game.play(0)
game.play(1)
game.play(2)
game.play(3)
game.play(4)
game.play(0)
game.play(0)
game.play(1)
game.play(1)
game.play(2)
game.play(2)
game.play(3) # Gana P2
print(game.play(1))


game.show()