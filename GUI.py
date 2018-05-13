from Tkinter import *
from random import choice
from numpy import array, dot, random

final = []


# Training
def clicTrain():
    unit_step = lambda x: 0 if x < 0 else 1
    training_data = [

        (array([l1c1, l1c2, l1c3,
                l2c1, l2c2, l2c3,
                l3c1, l3c2, l3c3,
                l4c1, l4c2, l4c3,
                l5c1, l5c2, l5c3,
                l6c1, l6c2, l6c3, 1]), 1),
    ]
    w = random.rand(1)
    errors = []
    eta = 0.2
    n = 100
    for i in xrange(n):
        x, expected = choice(training_data)
        result = dot(w, x)
        error = expected - unit_step(result)
        errors.append(error)
        w += eta * error * x
    for x, _ in training_data:
        result = dot(x, w)
        print (result)

        final = [nueboNumero + result]
        print final


# Identification
def clicId():
    unit_step = lambda x: 0 if x < 0 else 1
    training_data = [
        (array([l1c1, l1c2, l1c3,
                l2c1, l2c2, l2c3,
                l3c1, l3c2, l3c3,
                l4c1, l4c2, l4c3,
                l5c1, l5c2, l5c3,
                l6c1, l6c2, l6c3]), 1),
    ]
    w = random.rand(19)
    errors = []
    eta = 0.2
    n = 100
    for i in xrange(n):
        x, expected = choice(training_data)
        result = dot(w, x)
        error = expected - unit_step(result)
        errors.append(error)
        w += eta * error * x
    for x, _ in training_data:
        result = dot(x, w)

    for result, _ in final:
        elNumero = getint(nueboNumero)
        print elNumero


# Interface
GUI = Tk()
m2 = PanedWindow(orient=VERTICAL)
m2.pack(fill=BOTH, expand=1)
top = Label(m2)
m2.add(top)
middle = Label(m2)
m2.add(middle)
bottom = Label(m2)
m2.add(bottom)
# Ligne 1
l1c1 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=1, column=1)
l1c2 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=1, column=2)
l1c3 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=1, column=3)
# Ligne 2
l2c1 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=2, column=1)
l2c2 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=2, column=2)
l2c3 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=2, column=3)
# Ligne 3
l3c1 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=3, column=1)
l3c2 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=3, column=2)
l3c3 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=3, column=3)
# Ligne 4
l4c1 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=4, column=1)
l4c2 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=4, column=2)
l4c3 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=4, column=3)
# Ligne 5
l5c1 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=5, column=1)
l5c2 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=5, column=2)
l5c3 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=5, column=3)
# Ligne 6
l6c1 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=6, column=1)
l6c2 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=6, column=2)
l6c3 = Checkbutton(top, onvalue=1, offvalue=0).grid(row=6, column=3)

training = Button(middle, text="Train", command=clicTrain).pack(side=LEFT, padx=5, pady=5)
nueboNumero = Spinbox(middle, from_=0, to=9).pack(side=RIGHT, padx=5, pady=5)
id = Button(bottom, text="ID", command=clicId).pack(padx=5, pady=5)
lb = Label(bottom, text="Es el numero").pack(side=LEFT, padx=5, pady=5)
elNumero = Entry(bottom).pack(side=RIGHT, padx=5, pady=5)

# training.pack(side=LEFT, padx=5, pady=5)
# id.pack(padx=5, pady=5)

mainloop()
