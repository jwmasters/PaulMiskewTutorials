import tkinter as tk
import math

def submit():

    print("Submit pressed!")
    rad = float(entr.get())
    hei = float(enth.get())

    vol = math.pi*rad*rad*hei
    vol = round(vol, 3)

    output.config(state="normal")

    outputValue = "Given\n:radius:"+str(rad)+" units\nheight:"+str(hei)+" units\nThe volume is:"+str(vol)+" units cubed\n\n"
    output.delete(1.0, tk.END)
    output.insert(tk.INSERT, outputValue)
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