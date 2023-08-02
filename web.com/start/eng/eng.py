import tkinter as tk
from tkinter import ttk

def main():
    sitename = sitenameEntry.get()
    owndet = owndetEntry.get()

    if sitename == "" or owndet == "":
        print('Empty Sitename Field')
        return

    for obj in home:
        obj.pack_forget()
    runprog.pack()
    runLabel.pack()

    def progressUp(amount):
        runprog['value'] = amount
        root.update_idletasks()

    progressUp(10)

    createFolder = open(sitename+'/index.html','x')
    createFolder.close()

    progressUp(15)

    writeIndex = open(sitename+'/index.html')
    writeIndex.write(
f'''
<!DOCTYPE html>
<html>
<head>
    <title>{sitename}</title>
</head>
<body>
    <h1>Welcome to {sitename}! This site was created with web.com's START program. Visit start.web.com for more details. Unfortunately, this site hasn't been edited yet, so watch this space! This site is owned by {owndet}. If you would like to use this domain, contact them. If this site hasn't been updated ever, contact web.com.</h1>
</body>
</html>
'''
    )

    progressUp(30)

    createBot = open(sitename+'/bot','x')
    createBot.close()

    progressUp(50)

    createSetup = open(sitename+'/setup',"x")
    createSetup.close()

    progressUp(60)

    writeSetup = open(sitename+'/setup')
    writeSetup.write('start by web.com START.WEB.COM')
    writeSetup.close()

    progressUp(80)

    createOwndet = open(sitename+'/owndet','x')
    createOwndet.close()

    writeOwndet = open(sitename+'/owndet')
    writeOwndet.write(owndet)
    writeOwndet.close()

    progressUp(90)

    print('Cleaning Up')

    progressUp(100)
    
    runLabel.pack_forget()

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
runLabel = tk.Label(root, text="Running Setup Methods for Site..")
doneText = tk.Label(root, text="\nSuccessfully Created Site! You should be able to find it in the correct directory")
home = [titleLabel, sitenameLabel, sitenameEntry, owndetLabel, owndetEntry, startButton]

titleLabel.pack()
sitenameLabel.pack()
sitenameEntry.pack()
owndetLabel.pack()
owndetEntry.pack()
startButton.pack()
root.mainloop()