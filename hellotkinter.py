import tkinter as tk

root = tk.Tk()
root.title("Learning tkinterrr")  # window ka titile
root.geometry("300x200")  


label = tk.Label(root, text="Hello Tkinterr",font=("Arial",20))
label.pack()

def say_hello():
    print("Button clicked!")

button = tk.Button(root,text="click here",command=say_hello)
button.pack()

entry = tk.Entry(root, width=20)
entry.pack()

def show_input():
    print("You typed:" , entry.get())

button = tk.Button(root, text="Submit", command=show_input) 
button.pack()  

root. mainloop() 