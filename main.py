import tkinter as tk
# from scrapper import Scrapper

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.numberOfForms = 0
        # self.pack()
        self.create_scrapper_widgets()

    def create_scrapper_widgets(self):
        self.frame = tk.Frame(master=self.master, bg='#2b2d2f' )
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.titleframe = tk.Frame(master=self.frame, padx=10, pady=10, height=10, bg="#C0C0C0")
        self.titleframe.pack(fill=tk.X)
        self.titlelabel = tk.Label(master=self.titleframe, font=(None, 18), fg="#2b2d2f", text=f"Web scrapper", bg="#C0C0C0")
        self.titlelabel.pack()

        # self.initframe = tk.Frame(master=self.titleframe, padx=10, pady=10, height=100)
        # self.initframe.pack()

        # self.initlabel = tk.Label(master=self.initframe, text=f"Get pagination", font=(None, 15), padx=10, pady=10)
        # self.initlabel.grid(row=0, column=0, columnspan=2)

        # self.baseurllabel = tk.Label(master=self.initframe, text=f"base url", font=(None, 13), padx=10, pady=10)
        # self.baseurlentry = tk.Entry(master=self.initframe)
        # self.baseurllabel.grid(row=1, column=0)
        # self.baseurlentry.grid(row=1, column=1)

        # self.searchPathlabel = tk.Label(master=self.initframe, text=f"search path url", font=(None, 13), padx=10, pady=10)
        # self.searchPathentry = tk.Entry(master=self.initframe)
        # self.searchPathlabel.grid(row=2, column=0)
        # self.searchPathentry.grid(row=2, column=1)

        # self.mainframe = tk.Frame(master=self.master, padx=10, pady=10, height=10, relief=tk.RIDGE, borderwidth=5)
        # self.mainframe.pack(fill=tk.X)

        # self.submainframe = tk.Frame(master=self.mainframe, padx=10, pady=10, height=10)
        # self.submainframe.grid(row=0, column=0, columnspan=2)

        # self.addsearch = tk.Button(master=self.mainframe, font=(None, 13), padx=10, pady=10)
        # self.addsearch["text"] = "add search"
        # self.addsearch["command"] = self.addsearches
        # self.addsearch.grid(row=1, column=0, columnspan=2)


        self.submitframe = tk.Frame(master=self.frame, padx=10, pady=10, bg='#2b2d2f')
        self.submitframe.pack()
        
        self.runscrapperexe = tk.Button(master=self.submitframe, font=(None, 13), padx=5, pady=5)
        self.runscrapperexe["text"] = "Run scrapper"
        self.runscrapperexe["command"] = self.runScrapper
        self.runscrapperexe.pack()

    def addsearches(self):
        scrap_searches = []
        if self.numberOfForms < 2:
            formNum = self.numberOfForms
            print(self.numberOfForms)
            scrap_searches.append(self.addsearchForm(formNum))
            self.numberOfForms = formNum + 1
            self.mainframe = scrap_searches
        # entries = []
        # for field in 'base url', 'search url':
        #     entries.append(LabelEntry(frame, field, button))

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")

    def addsearchForm(self, formNumber):
        formName = 'addframe' + str(formNumber)
        self.formName = tk.Frame(master=self.submainframe, padx=10, pady=10, height=100, relief=tk.RIDGE, borderwidth=5)
        self.formName.grid(row=str(formNumber), column=0, columnspan=2)

        self.initlabel = tk.Label(master=self.formName, text='Form ' + str(formNumber + 1), font=(None, 15), padx=10, pady=10)
        self.initlabel.grid(row=0, column=0, columnspan=2)

        self.baseurllabel = tk.Label(master=self.formName, text=f"Search url", font=(None, 13), padx=10, pady=10)
        self.baseurlentry = tk.Entry(master=self.formName, width=40)
        self.baseurllabel.grid(row=1, column=0)
        self.baseurlentry.grid(row=1, column=1)

        self.filelabel = tk.Label(master=self.formName, text=f"Temp file", font=(None, 13), padx=10, pady=10)
        self.fileentry = tk.Entry(master=self.formName, width=40)
        self.filelabel.grid(row=1, column=0)
        self.fileentry.grid(row=1, column=1)
     
        self.cleanfilelabel = tk.Label(master=self.formName, text=f"Clean temp file", font=(None, 13), padx=10, pady=10)
        self.cleanfileentry = tk.Entry(master=self.formName, width=40)
        self.cleanfilelabel.grid(row=2, column=0)
        self.cleanfileentry.grid(row=2, column=1)

        self.subfilelabel = tk.Label(master=self.formName, text=f"Sub temp file", font=(None, 13), padx=10, pady=10)
        self.subfileentry = tk.Entry(master=self.formName, width=40)
        self.filelabel.grid(row=3, column=0)
        self.fileentry.grid(row=3, column=1)
     
        self.subcleanfilelabel = tk.Label(master=self.formName, text=f"Clean sub temp file", font=(None, 13), padx=10, pady=10)
        self.subcleanfileentry = tk.Entry(master=self.formName, width=40)
        self.subcleanfilelabel.grid(row=4, column=0)
        self.subcleanfileentry.grid(row=4, column=1)

        self.text_box = tk.Text(master=self.formName)
        self.text_box.grid(row=0, column=3, rowspan=5, padx=10, pady=10)

    def runScrapper(self):
        # scanSite = Scrapper("https://jobs.sanctuary-group.co.uk/search/")
        # scanSite.get_web_content('test2.txt')
        baseurl = self.baseurlentry.get()
        searchurl = self.searchPathentry.get()
        print(baseurl)
        print(searchurl)

root = tk.Tk()
app = Application(master=root)
app.mainloop()