from tkinter import *
from logic import log
import threading

class vis(log):
    def __init__(self):
        super().__init__()

        root = Tk()

        l1 = Label(root, text="Формула").pack()

        l2 = Label(root, text="Количество особей").pack()
        self.e1 = Entry(root)
        self.e1.pack()

        l3 = Label(root, text="Нижняя граница Х").pack()
        self.e2 = Entry(root)
        self.e2.pack()

        l4 = Label(root, text="Верхняя граница Х").pack()
        self.e3 = Entry(root)
        self.e3.pack()

        l5 = Label(root, text="Нижняя граница Y").pack()
        self.e4 = Entry(root)
        self.e4.pack()

        l6 = Label(root, text="Верхняя граница Y").pack()
        self.e5 = Entry(root)
        self.e5.pack()

        b1 = Button(root, text = "Получить первую популяцию", command = self.first_).pack()
        b2 = Button(root, text = "Новая популяция", command = self.next_).pack()
        b3 = Button(root, text = "Все популяции", command = self.all_).pack()

        self.t1 = Text(root)
        self.t1.pack()
        self.text = self.t1

        root.mainloop()

    def first_(self):
        self.get()
        x = threading.Thread(target=self.first)
        x.start()

    def all_(self):
        self.get()
        x = threading.Thread(target = self.all)
        x.start()

    def next_(self):
        self.get()
        x = threading.Thread(target=self.next)
        x.start()

    def get(self):
        self.n = int(self.e1.get())
        self.min_x = int(self.e2.get())
        self.max_x = int(self.e3.get())
        self.min_y = int(self.e4.get())
        self.max_y = int(self.e5.get())