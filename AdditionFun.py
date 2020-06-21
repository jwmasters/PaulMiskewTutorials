import tkinter as tk
import random
#use the import os for the MAC or IOS platforms
#import os

nums = [3, 4]
size = 36
btnSize = 18
txtSize = 12

def runMe():
    print("Running")
    result = int(entry.get())
    motivationResponse = ""

    if result == nums[0] + nums[1]:
        entry.config(bg="white")
        print("Correct")
        nums[0] = random.randint(0, 10)
        nums[1] = random.randint(0, 10)

        num1Label.config(text=nums[0])
        num2Label.config(text=nums[1])
        entry.delete(0, tk.END)

        randNum = random.randint(0, 4)

        if (randNum == 0):
            #os.system("say good job")
            print("good job")
            motivationResponse = "good job"
        elif (randNum == 1):
            #os.system("say great work!")
            print("great work!")
            motivationResponse = "great work!"
        elif (randNum == 2):
            #os.system("say spectacular")
            print("spectacular")
            motivationResponse = "spectacular"
        else:
            #os.system("say keep going!")
            print("keep going!")
            motivationResponse = "Keep going!"

        #output.config(state="normal")
        #outputValue = motivationResponse
        #output.delete(1.0, tk.END)
        #output.insert(tk.INSERT, outputValue)
        #output.config(state="disabled")
    else:
        print("ERROR")
        motivationResponse = "Oops, try again!"
        entry.delete(0, tk.END)
        entry.config(bg="red")

    output.config(state="normal")
    outputValue = motivationResponse
    output.delete(1.0, tk.END)
    output.insert(tk.INSERT, outputValue)
    output.config(state="disabled")


def say():
    print("Says the question")
    #statement = str(nums[0]) + "+" + str(nums[1]) + " = what"
    #os.system("Say " + statement)


root = tk.Tk()
root.title("Add Practice")
root.maxsize(600, 700)
root.minsize(250, 300)

num1Label = tk.Label(root, text=str(nums[0]), font=("Helvetica", size))
num1Label.grid(row=0, column=0)

operationLabel = tk.Label(root, text="+", font=("Helvetica", size))
operationLabel.grid(row=0, column=1)

num2Label = tk.Label(root, text=str(nums[1]), font=("Helvetica", size))
num2Label.grid(row=0, column=2)

equalLabel = tk.Label(root, text="=", font=("Helvetica", size))
equalLabel.grid(row=0, column=3)

entry = tk.Entry(root, width=4, font=("Helvetica", size))
entry.grid(row=0, column=4)

checkbtn = tk.Button(root, text="Check your answer.", highlightbackground="#3E4149", font=("Helvetica", btnSize), command=runMe)
checkbtn.grid(row=1, column=0, columnspan=5, sticky="nesw")

speakbtn = tk.Button(root, text="Speak to me!", highlightbackground="#3E4149", font=("Helvetica", btnSize), command=say)
speakbtn.grid(row=2, column=0, columnspan=5, sticky="nesw")

output = tk.Text(root, width=20, height=5, borderwidth=3, relief=tk.GROOVE, font=("Helvetica", txtSize))
output.config(state="disabled")
output.grid(row=3, column=0, columnspan=5, sticky="nesw")

root.mainloop()