import tkinter as tk
from tkhtmlview import HTMLLabel

def read_html(open_file):
    with open(open_file, "r") as source:
        html_content = source.read()
    html_label.set_html(html_content)

def go():
    file_path = sourceGet.get()
    read_html(file_path)

root = tk.Tk()
root.title("Linker")

html_label = HTMLLabel(root, html="")
html_label.pack()

sourceGet = tk.Entry(root)
sourceGet.pack()

load_button = tk.Button(root, text="Load HTML", command=go)
load_button.pack()

root.mainloop()