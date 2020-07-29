import tkinter as tk

class SearchForm:
    def __init__(self, master, gridPos):
        self.master = master
        self.gridPos = gridPos        
        self.url = ''
        self.filepath = ''
        self.row = ''
        self.column = ''
    
    def showForm(self):
        x = self.gridPos[0]
        y = self.gridPos[1]

        self.formName = tk.Frame(
            master=self.master,
            relief=tk.RIDGE,
            borderwidth=5,
            padx=10,
            pady=10,
            bg="#2b2d2f",
        )
        self.formName.grid(row=x, column=y)

        self.initlabel = tk.Label(
            master=self.formName,
            text="Search ",
            font=(None, 13),
            padx=10,
            pady=10,
            fg="#C0C0C0",
            bg="#2b2d2f",
        )
        self.initlabel.grid(row=0, column=0, columnspan=2)

        self.baseurllabel = tk.Label(
            master=self.formName,
            text=f"Search url: ",
            font=(None, 12),
            padx=10,
            pady=10,
            fg="#C0C0C0",
            bg="#2b2d2f",
        )
        self.baseurllabel.grid(row=1, column=0)

        # Search url entry
        self.url = tk.Entry(master=self.formName, width=40)
        self.url.grid(row=1, column=1)

        self.pathlabel = tk.Label(
            master=self.formName,
            text=f"Save file to: ",
            font=(None, 12),
            padx=10,
            pady=10,
            fg="#C0C0C0",
            bg="#2b2d2f",
        )
        self.pathlabel.grid(row=2, column=0)

        # file path entry
        self.filepath = tk.Entry(master=self.formName, width=40)
        self.filepath.grid(row=2, column=1)

        self.rowlabel = tk.Label(
            master=self.formName,
            text=f"Row expression: ",
            font=(None, 12),
            padx=10,
            pady=10,
            fg="#C0C0C0",
            bg="#2b2d2f",
        )

        self.rowlabel.grid(row=3, column=0)

        # Expression to find row
        self.row = tk.Entry(master=self.formName, width=40)
        self.row.grid(row=3, column=1)

        self.subformName = tk.Frame(master=self.formName, bg="#2b2d2f")
        self.subformName.grid(row=4, column=0, columnspan=2)

        self.columnlabel = tk.Label(
            master=self.subformName,
            text=f"Column expressions",
            font=(None, 12),
            padx=10,
            pady=10,
            fg="#C0C0C0",
            bg="#2b2d2f",
        )
        self.columnlabel.grid(row=0, column=0)

        # Column expressions entry
        self.column = tk.Text(master=self.subformName, width=50, height = 25)
        self.column.grid(row=1, column=0)

    def getFormUrl(self):
        url = self.url.get()
        return url

    def getFormFilePath(self):
        filepath = self.filepath.get()
        return filepath

    def getFormRow(self):
        row = self.row.get()
        return row

    def getFormColumn(self):
        column = self.column.get("1.0", tk.END)
        return column