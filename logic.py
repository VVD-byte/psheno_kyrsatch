import random
import tkinter as tk
import math

class log:
    def __init__(self):
        self.n = 6
        self.min_x = -5
        self.max_x = 5
        self.min_y = -5
        self.max_y = 5
        self.text = ''
        self.gen = [1 for i in range(self.n)]
        self.go = True
        self.exp = 2.718

    def yravn(self, x, y):
        return -self.exp**(-0.2*math.sqrt(x**2 + y**2) + 3*(math.cos(2*x) + math.sin(2*y)))

    def all(self):
        self.first()
        while self.go:
            self.next()

    def first(self):
        self.text.delete('1.0', tk.END)
        self.gen = [self.get_x_y() for i in range(self.n)]
        self.text_print()

    def next(self):
        if self.go:
            self.mutation()
            self.text_print()

    def mutation(self):
        self.gen.sort(key=lambda x: x[2])
        max_ = self.gen[-1][2]
        self.gen = [self.gen[-1] for i in range(self.n)]
        self.gen[:self.n//2], self.gen[self.n//2:] = [self.get_x__(i[0]) for i in self.gen[:self.n//2]], [self.get__y(i[1]) for i in self.gen[self.n//2:]]
        if True not in [i[2] > max_ for i in self.gen]: self.go = False

    def get_x_y(self):
        x, y = round(random.uniform(self.min_x, self.max_x), 1), round(random.uniform(self.min_y, self.max_y), 1)
        return (x, y, self.yravn(x, y))

    def get__y(self, y):
        x = round(random.uniform(self.min_x, self.max_x), 1)
        return (x, y, self.yravn(x, y))

    def get_x__(self, x):
        y = round(random.uniform(self.min_y, self.max_y), 1)
        return (x, y, self.yravn(x, y))

    def text_print(self):
        for i in self.gen:
            self.text.insert(tk.END, f'{i[0]}\t{i[1]}\t{i[2]}\n')
        self.text.insert(tk.END, '\n')