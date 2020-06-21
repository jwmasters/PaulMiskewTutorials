import tkinter as tk

class Display:

    def __init__(self):
        print("Constructing Object")
        self.root = tk.Tk()
        self.root.title("Option Menu Class")
        self.root.maxsize(600, 500)
        self.root.minsize(500, 400)

        self.OPTIONS = ["eggs", "bunny", "chicken"]

        self.var = tk.StringVar(self.root)
        self.var.set(self.OPTIONS[0])
        self.var.trace("w", self.change)

        self.dropDownMenu = tk.OptionMenu(self.root, self.var, self.OPTIONS[0], self.OPTIONS[1], self.OPTIONS[2])
        self.dropDownMenu.pack()

        self.root.mainloop()

    def change(self, *args):
        print("changing")
        print(self.var.get())

#https://www.youtube.com/watch?v=9zuFYi0ZzbQ&list=PLXPfOoCLXkKahgyuQZpn8VOCDBJaGFmB8&index=35
#Paul Miskew Channel


display1 = Display()