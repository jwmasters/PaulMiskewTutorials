import tkinter as tk
import math

class CylinderCalc:

    def __init__(self):

        print("Creating Cylinder Calculator Object")

        self.root = tk.Tk()
        self.root.title("Cylinder Calculator")
        self.root.maxsize(600, 500)
        self.root.minsize(500, 400)

        self.labr = tk.Label(self.root, text="radius")
        self.labr.pack()

        self.entr = tk.Entry(self.root)
        self.entr.pack()

        self.labh = tk.Label(self.root, text="height")
        self.labh.pack()

        self.enth = tk.Entry(self.root)
        self.enth.pack()

        self.btn = tk.Button(self.root, text="Calculate")
        self.btn.pack()

        self.output = tk.Text(self.root, height=15, width=50, borderwidth=5, relief=tk.GROOVE)
        self.output.configure(state="disabled")
        self.output.pack()

        self.root.mainloop()

cylindercalc = CylinderCalc()