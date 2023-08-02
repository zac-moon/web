import tkinter as tk
from tkinter import ttk

def main():
    runprog['value'] = 0

    for obj in home:
        obj.pack_forget()
    runprog.pack()

    def progressUp(amount):
        runprog['value'] = amount
        root.update_idletasks()

    sitename = sitenameEntry.get()
    owndet = owndetEntry.get()

    # Check if either entry is empty
    if not sitename:
        sitenameEntry.config(highlightthickness=2, highlightbackground='red')
    else:
        sitenameEntry.config(highlightthickness=0)
    if not owndet:
        owndetEntry.config(highlightthickness=2, highlightbackground='red')
    else:
        owndetEntry.config(highlightthickness=0)

    progressUp(10)

root = tk.Tk()
root.title('start by web.com | Engine')
root.geometry('700x300')

titleLabel = tk.Label(root, text='WELCOME TO START by WEB.COM!\nPlease enter in a few details so we can set your site up for you. Once entered, details are irreversible.')

sitenameLabel = tk.Label(root, text="\n\nEnter name for your site (e.g. example.com) :")
sitenameEntry = tk.Entry(root)

owndetLabel = tk.Label(root, text="\n\nEnter a name to be recognised as the owner OWNER DETAILS (e.g. a Person or Company. \nCan be Firstname Lastname with Company Inc. (Can help to provide company's main website if they have one.))")
owndetEntry = tk.Entry(root)

startButton = tk.Button(root, text="Start", command=main)

runprog = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')

home = [titleLabel, sitenameLabel, sitenameEntry, owndetLabel, owndetEntry, startButton]

titleLabel.pack()
sitenameLabel.pack()
sitenameEntry.pack()
owndetLabel.pack()
owndetEntry.pack()
startButton.pack()
root.mainloop()