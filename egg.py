import random
import time
import os
import sys

class PICK(object):
        def __init__(self):
                self.round = 0
                self.count = 100
                self.broke=[]
                self.balls = []
                self.bar = [[5,3],[5,4],[5,5]]
        def matrixprint(self):
                matrix = [[' ']*10 for i in range(7)]
                for i in range(7):
                        matrix[i][0],matrix[i][9]='|','|'
                for i in self.balls:
                        matrix[i[0]][i[1]] = 'O'
                for i in self.bar:
                        matrix[5][i[1]] = '='
                for i in self.broke:
                        matrix[6][i[1]] = 'X'
                print ('\n'.join([''.join(line) for line in matrix]))
        def create(self):
                random.seed(time.time())
                r = random.randint(1,8)
                self.balls.append([0,r])
        def pickup(self):
                mark = None
                for b in range(len(self.balls)):
                        if self.balls[b] in self.bar:
                                mark = b
                if mark != None:
                        self.balls.pop(mark)
                self.round += 1
                if self.round >= 50:
                        print('You Win! Good Job!')
                        input()
                        sys.exit()
        def move(self,m):
                if 3<self.bar[2][1]<8:
                        for k in range(len(self.bar)):
                                self.bar[k][1] += m
                                self.bar[k][1] = max(min(self.bar[k][1],8),1)
                elif self.bar[2][1] == 3:
                        if m == 1:
                                for k in range(len(self.bar)):
                                        self.bar[k][1] += m
                elif self.bar[2][1] == 8:
                        if m == -1:
                                for k in range(len(self.bar)):
                                        self.bar[k][1] += m
        def drop(self):
                d=[(1,-1),(1,0),(1,1)]
                for b in range(len(self.balls)):
                        n = random.randint(0,2)
                        self.balls[b][0] += d[n][0]
                        self.balls[b][1] += d[n][1]
                        self.balls[b][1] = max(min(self.balls[b][1],8),1)
        def broken(self):
                self.broke=[]
                markb = None
                for b in range(len(self.balls)):
                        if self.balls[b][0] > 5:
                                markb = b
                if markb != None:
                        self.broke.append(self.balls.pop(markb))
                        self.count -= 20
                if self.count <= 0:
                        o = os.system('cls')
                        print ('Welcome to play Pickup Game!')
                        print ('Your current count: %d' % pk.count)
                        pk.matrixprint()
                        print('You Lose! Game Over!')
                        input()
                        sys.exit()

pk=PICK()
while True:
        o = os.system('cls')
        print ('Welcome to play Pickup Game!')
        print ('Your current count: %d' % pk.count)
        if pk.round % 3 == 0 or pk.round % 7 == 0:
                pk.create()
        pk.matrixprint()
        print('You want to move "Left for A", "Stay for S" or "Right for D"?')
        mov = input('>>>')
        if mov == 'A' or mov == 'a':
                m = -1
        elif mov == 'D' or mov == 'd':
                m = 1
        elif mov == 'S' or mov == 's':
                m = 0
        else:
                m = 0
                print('Wrong Input!')
                input()
        pk.move(m)
        pk.drop()
        pk.pickup()
        pk.broken()