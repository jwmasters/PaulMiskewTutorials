import tkinter as tk
import math

def submit():

    print("Submit pressed!")
    rad = float(entr.get())
    hei = float(enth.get())

    v = math.pi*rad*rad*hei
    v = round(v, 3)

    output.config(state="normal")
    output.insert(tk.INSERT, v)
    output.config(state="disabled")


root = tk.Tk()
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="Radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="Height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

#https://www.youtube.com/watch?v=d4k8-z_ZKfE&list=PLXPfOoCLXkKahgyuQZpn8VOCDBJaGFmB8&index=28
#Paul Miskew 

root.mainloop()