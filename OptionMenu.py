import tkinter as tk


def change(*args):
    print("running change")
    print(var.get())

root = tk.Tk()
root.title("Option Menu")

OPTIONS = [
    "eggs",
    "bunney",
    "chicken",
]

var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w", change)

dropDownMenu = tk.OptionMenu(root, var, OPTIONS[0], OPTIONS[1], OPTIONS[2])
dropDownMenu.pack()


root.mainloop()
print("End program")