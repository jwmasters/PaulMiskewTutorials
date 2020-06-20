import tkinter as tk

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

btn = tk.Button(root, text="Submit")
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.pack()
#https://www.youtube.com/watch?v=d4k8-z_ZKfE&list=PLXPfOoCLXkKahgyuQZpn8VOCDBJaGFmB8&index=28
#Paul Miskew 

root.mainloop()