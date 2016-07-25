# Evolution-game (Python 2.7)
#!/usr/bin/env python
class cell:
    def __init__(self,data,hp,xy):
        self.data = data
        self.hp = hp
    def update(self):
        self.hp -= 1
        try:
            exec self.data[self.data[0]]
            self.data[0] += 1
        except:
            exec self.data[1]
            self.data[0] = 2
    def move(self,x,y):
        self.xy[0] += x
        self.xy[1] += y

cells = []









