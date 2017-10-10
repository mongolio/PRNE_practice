import Tkinter as tk


def printNum(num):
    """"""
    print "You pressed the %s button" % num

parent = tk.Tk()
frame = tk.Frame(parent)
frame.pack()

btn22 = tk.Button(frame,
                  text="22", command=lambda: printNum(22))
btn22.pack(side=tk.LEFT)

btn44 = tk.Button(frame,
                  text="44", command=lambda: printNum(44))
btn44.pack(side=tk.LEFT)
parent.mainloop()
