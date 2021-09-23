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
        for i in self.table:
            sum=0
            for k in i:
                if k==self.player:
                    sum+=1
                elif sum==4:
                    self.keep_playing=False
                    self.winner=self.player
                    return self
        for i in self.table.T:
            sum=0
            for k in i:
                if k==self.player:
                    sum+=1
                elif sum==4:
                    self.keep_playing=False
                    self.winner=self.player
                    return self
            # for i in range(3,len(self.table[0])):
            #     sum=0
            #     for k in range(0,4):
            #         sum+=self.table[i][k]
            #     if sum==self.player*4:
            #         self.keep_playing=False
            #         self.winner=self.player
    
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
                            return self
                    except IndexError:
                        self.table[col_place][i]=self.player
                        self.check()
                        self.change_player()
                        return self
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
game.play(0) # Gana P2
game.play(3)
game.play(6)
game.play(3)
print(game.play(4))
# print(game.play(1))


game.show()