import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile

root = Tk()



def ask_open_file_and_get():
    file = askopenfile(mode ='r', filetypes =[('Csv files', '*.csv')])
    if file:
        data = pd.read_csv(file.name)
        cols = tuple(data.keys())
        tree = Treeview(root, columns=cols, show='headings')
        scrollbar = Scrollbar(root, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        db = []
        for i in cols:
            tree.heading(i, text=i)
            db.append(tuple(data[i]))
        
        c = range(len(db[-1]))
        for p in c:
            aw = []
            for k in range(len(cols)):
                aw.append(str(db[k][p]))
            tree.insert("", END, values=tuple(aw))

        tree.grid(row=0, column=0, sticky='nsew')

        fr1 = Frame(root)

    

        fr1.grid(row=0, column=2)
            

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=ask_open_file_and_get)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()