import tkinter as tk
from searchform import SearchForm
# from scrapper import Scrapper


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.numberOfForms = 0
        # self.searchform = SearchForm()
        self.storeFormInputs = []
        # self.pack()
        self.create_scrapper_widgets()

    def create_scrapper_widgets(self):
        self.frame = tk.Frame(master=self.master, bg="#2b2d2f")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.titleframe = tk.Frame(
            master=self.frame, padx=10, pady=10, height=10, bg="#C0C0C0"
        )
        self.titleframe.pack(fill=tk.X)
        self.titlelabel = tk.Label(
            master=self.titleframe,
            font=(None, 18),
            fg="#2b2d2f",
            text=f"Web scrapper",
            bg="#C0C0C0",
        )
        self.titlelabel.pack()

        self.topframe = tk.Frame(
            master=self.frame, padx=10, pady=10, height=10, bg="#2b2d2f"
        )
        self.topframe.pack(fill=tk.X)

        self.baseurllabel = tk.Label(
            master=self.topframe,
            text=f"Base url: ",
            font=(None, 13),
            padx=10,
            pady=10,
            fg="#C0C0C0",
            bg="#2b2d2f",
        )

        self.baseurllabel.grid(row=0, column=0)

        self.baseurlentry = tk.Entry(master=self.topframe, width=50)
        self.baseurlentry.grid(row=0, column=1)

        self.searchPathlabel = tk.Label(
            master=self.topframe,
            text=f"Path url: ",
            font=(None, 13),
            padx=10,
            pady=10,
            fg="#C0C0C0",
            bg="#2b2d2f",
        )

        self.searchPathlabel.grid(row=0, column=2)

        self.subdomainPathentry = tk.Entry(master=self.topframe, width=50)
        self.subdomainPathentry.grid(row=0, column=3)

        self.mainframe = tk.Frame(
            master=self.frame, padx=10, pady=10, height=10, bg="#2b2d2f"
        )
        self.mainframe.pack(fill=tk.X)

        self.addsearchlabel = tk.Label(
            master=self.mainframe,
            text=f"Add child page search: ",
            font=(None, 13),
            padx=10,
            pady=10,
            fg="#C0C0C0",
            bg="#2b2d2f",
        )
        self.addsearchlabel.grid(row=0, column=0)

        self.addsearch = tk.Button(
            master=self.mainframe, font=(None, 13), padx=5, pady=5
        )
        self.addsearch["text"] = "Add search"
        self.addsearch["command"] = self.addsearches
        self.addsearch.grid(row=0, column=1)

        self.submainframe = tk.Frame(
            master=self.frame, padx=20, pady=10, height=10, bg="#2b2d2f"
        )
        self.submainframe.pack(fill=tk.X)

        self.submitframe = tk.Frame(master=self.frame, padx=10, pady=10, bg="#2b2d2f")
        self.submitframe.pack()

        self.runscrapperexe = tk.Button(
            master=self.submitframe, font=(None, 13), padx=5, pady=5
        )
        self.runscrapperexe["text"] = "Run scrapper"
        self.runscrapperexe["command"] = self.runScrapper
        self.runscrapperexe.pack()

    def addsearches(self):
        row = 2
        column = 2
        value = self.numberOfForms
        if value < 2:
            grids = self.grid(row, column)
            self.addsearchForm(value, grids[value])
        self.numberOfForms += 1

    def grid(self, row, column):
        grids = []
        for i in range(row):
            for j in range(column):
                grids.append([i, j])
        return grids


        #         grid.append([])
        #         grid[-1].append(0)
        # rows += 1
        # print(grid)

        # scrap_searches = []
        # if self.numberOfForms < 2:
        #     formNum = self.numberOfForms
        #     print(self.numberOfForms)
        #     scrap_searches.append(self.addsearchForm(formNum))
        #     self.numberOfForms = formNum + 1
        #     self.mainframe = scrap_searches
        # entries = []
        # for field in 'base url', 'search url':
        #     entries.append(LabelEntry(frame, field, button))

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")

    # Create instances of searchform and save
    def addsearchForm(self, formNumber, gridPos):
        searchR = SearchForm(self.submainframe, gridPos)
        searchR.showForm()
        self.storeFormInputs.append(searchR)

    def runScrapper(self):
        # Get base url value
        print(self.baseurlentry.get())
        print(self.subdomainPathentry.get())

        # for i in self.storeFormInputs.items():
        #     print(i.getFormUrl())
        #     print(i.getFormFilePath())
        #     print(i.getFormRow())
        #     print(i.getFormColumn())

        # Get values from instances
        print(self.storeFormInputs[0].getFormUrl())
        print(self.storeFormInputs[0].getFormFilePath())
        print(self.storeFormInputs[0].getFormRow())
        print(self.storeFormInputs[0].getFormColumn())

        print(self.storeFormInputs[1].getFormUrl())
        print(self.storeFormInputs[1].getFormFilePath())
        print(self.storeFormInputs[1].getFormRow())
        print(self.storeFormInputs[1].getFormColumn())

root = tk.Tk()
app = Application(master=root)
app.mainloop()
