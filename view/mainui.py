import tkinter as tk
import tkinter.ttk as ttk
from searchWidget import SearchWidget
# from scrapper import Scrapper


class MainUi(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.numberOfSearchWidgets = 0
        self.storeValue = {}
        # self.searchform = SearchForm()
        # self.storeFormInputs = []
        # self.pack()
        # self.create_scrapper_widgets()
        self.__createStyle()
        self.__createWIdget()
        self.__title()
        self.__add_widgets()
        self.__add_widgets_content()
        self.__submit()
        # self.add_button()
        # self.content_section()
        # self.run_scrap_section()
        # self.run_button()

    def __createStyle(self):
        self.s = ttk.Style()
        self.s.configure('m.TFrame', background='#2b2d2f', border=100)
        self.s.configure('mt.TFrame', background='#C0C0C0')
        self.s.configure('i.TFrame', padding=10, background='#2b2d2f', foreground='#2b2d2f')
        self.s.configure('mt.TLabel', background='#C0C0C0', foreground='#2b2d2f', font=(None, 18), padding=10)
        self.s.configure('add.TLabel', background='#2b2d2f', foreground='#C0C0C0', font=(None, 14), padding=20)
        self.s.configure('add.TButton', background='#C0C0C0', foreground='#2b2d2f', font=(None, 14), padding=10)
        self.s.configure('s.TFrame', background='#2b2d2f', font=(None, 14), padding=10)

        # self.s.configure('App.TFrame', background='yellow')
        # self.s.configure('Btn.TButton', background='light blue', border=10)

    def __createWIdget(self):
        self.frame = ttk.Frame(master=self.master, style='m.TFrame')
        self.frame.pack(fill=tk.BOTH)

    def __title(self):
        self.titleframe = ttk.Frame(
            master=self.frame, 
            style='mt.TFrame'
        )
        self.titleframe.pack(fill=tk.X)
        self.titlelabel = ttk.Label(
            master=self.titleframe,
            text='Web Scrapper',
            style='mt.TLabel'
        )
        self.titlelabel.pack()

    def __add_widgets(self):
        self.innerframe = ttk.Frame(master=self.frame, style='i.TFrame')
        self.innerframe.pack(fill=tk.X)

        self.addWidgetLabel = ttk.Label(
            master=self.innerframe,
            text='Add child page search: ',
            style='add.TLabel'
        )
        self.addWidgetLabel.pack(side='left')

        self.addWidgetButton = ttk.Button(
            master=self.innerframe,
            style='add.TButton'
        )
        self.addWidgetButton['text'] = 'Add widget'
        self.addWidgetButton["command"] = self.addwidgets
        self.addWidgetButton.pack(side='left')

    def __add_widgets_content(self):
        self.add_content_frame = ttk.Frame(master=self.frame, style="i.TFrame")
        self.add_content_frame.pack(fill=tk.X)  


    def addwidgets(self):
        value = self.numberOfSearchWidgets
        if value < 3:
            # grids = self.grid(row, column)
            SearchWidget(self.add_content_frame, self)
            self.numberOfSearchWidgets += 1      

    def __submit(self):
        self.submitFrame = ttk.Frame(
            master=self.frame, 
            style='s.TFrame'
        )
        self.submitFrame.pack(fill=tk.X)

        self.submitButton = ttk.Button(
            master=self.submitFrame,
            style='add.TButton'
        )
        self.submitButton['text'] = 'Run scrapper'
        self.submitButton["command"] = self.runProcess
        self.submitButton.pack()

    def runProcess(self):
        for i in self.storeValue:
            print(i)

    # def add_button(self):
    #     self.addWidgetLabel = ttk.Label(
    #         master=self.add_content_frame,
    #         text='Add child page search: ',
    #         style='add.TLabel'
    #     )
    #     self.addWidgetLabel.grid(row=0, column=0)

    #     self.addSearchButton = ttk.Button(
    #         master=self.add_content_frame,
    #         style='add.TButton'
    #     )
    #     self.addSearchButton["text"] = "Add search"
    #     # self.addsearch["command"] = self.addwidgets
    #     self.addSearchButton.grid(row=0, column=1)

    # def content_section(self):
    #     self.content_frame = tk.Frame(master=self.innerframe, bg="#2b2d2f", padx=20)
    #     self.content_frame.pack(fill=tk.BOTH, expand=True)

    # def addwidgets(self):
    #     row = 2
    #     column = 3
    #     value = self.numberOfSearchWidgets
    #     if value < 3:
    #         grids = self.grid(row, column)
    #         self.addsearchWidgets(grids[value])
    #         self.numberOfSearchWidgets += 1

    # def grid(self, row, column):
    #     grids = []
    #     for i in range(row):
    #         for j in range(column):
    #             grids.append([i, j])
    #     return grids

    # def addsearchWidgets(self, gridPos):
    #     searchR = SearchWidget(self.content_frame, gridPos, self)
    #     pass
        # searchR.showForm()
        # self.storeFormInputs.append(searchR)
        # pass
            #         grid.append([])
            #         grid[-1].append(0)
            # rows += 1
            # print(grid)

            # scrap_widgets = []
            # if self.numberOfForms < 2:
            #     formNum = self.numberOfForms
            #     print(self.numberOfForms)
            #     scrap_widgets.append(self.addsearchWidgets(formNum))
            #     self.numberOfForms = formNum + 1
            #     self.mainframe = scrap_widgets
            # entries = []
            # for field in 'base url', 'search url':
            #     entries.append(LabelEntry(frame, field, button))

            # self.quit = tk.Button(self, text="QUIT", fg="red",
            #                       command=self.master.destroy)
            # self.quit.pack(side="bottom")


    # def run_scrap_section(self):
    #     self.run_scrap = tk.Frame(master=self.innerframe, bg="#2b2d2f", padx=20, pady=10)
    #     self.run_scrap.pack(fill=tk.BOTH, expand=True)

    # def run_button(self):
    #     self.run_search = tk.Button(
    #         master=self.run_scrap, font=(None, 13), padx=5, pady=5
    #     )
    #     self.run_search["text"] = "Run scrapper"
    #     # self.addsearch["command"] = self.addwidgets
    #     self.run_search.pack()

















    # def create_scrapper_widgets(self):






    #     self.topframe = tk.Frame(
    #         master=self.frame, padx=10, pady=10, height=10, bg="#2b2d2f"
    #     )
    #     self.topframe.pack(fill=tk.X)

    #     self.baseurllabel = tk.Label(
    #         master=self.topframe,
    #         text=f"Base url: ",
    #         font=(None, 13),
    #         padx=10,
    #         pady=10,
    #         fg="#C0C0C0",
    #         bg="#2b2d2f",
    #     )

    #     self.baseurllabel.grid(row=0, column=0)

    #     self.baseurlentry = tk.Entry(master=self.topframe, width=50)
    #     self.baseurlentry.grid(row=0, column=1)

    #     self.searchPathlabel = tk.Label(
    #         master=self.topframe,
    #         text=f"Path url: ",
    #         font=(None, 13),
    #         padx=10,
    #         pady=10,
    #         fg="#C0C0C0",
    #         bg="#2b2d2f",
    #     )

    #     self.searchPathlabel.grid(row=0, column=2)

    #     self.subdomainPathentry = tk.Entry(master=self.topframe, width=50)
    #     self.subdomainPathentry.grid(row=0, column=3)

    #     self.mainframe = tk.Frame(
    #         master=self.frame, padx=10, pady=10, height=10, bg="#2b2d2f"
    #     )
    #     self.mainframe.pack(fill=tk.X)

    #     self.addWidgetLabel = tk.Label(
    #         master=self.mainframe,
    #         text=f"Add child page search: ",
    #         font=(None, 13),
    #         padx=10,
    #         pady=10,
    #         fg="#C0C0C0",
    #         bg="#2b2d2f",
    #     )
    #     self.addWidgetLabel.grid(row=0, column=0)



    #     self.submainframe = tk.Frame(
    #         master=self.frame, padx=20, pady=10, height=10, bg="#2b2d2f"
    #     )
    #     self.submainframe.pack(fill=tk.X)

    #     self.submitframe = tk.Frame(master=self.frame, padx=10, pady=10, bg="#2b2d2f")
    #     self.submitframe.pack()

    #     self.runscrapperexe = tk.Button(
    #         master=self.submitframe, font=(None, 13), padx=5, pady=5
    #     )
    #     self.runscrapperexe["text"] = "Run scrapper"
    #     self.runscrapperexe["command"] = self.runScrapper
    #     self.runscrapperexe.pack()



    # Create instances of searchform and save


    # def runScrapper(self):
    #     print('Testing')
        # try:
        #     scrapper_url = self.baseurlentry.get()
        #     scrap_base = Scrapper(scrapper_url)

        #     sub_domain = self.subdomainPathentry.get()
        #     scrap_base.init_page_scan('//ul[@class="pagination"]/li/a/@href', sub_domain)

        # except NameError:
        #     print ("This variable is not defined")
        # else:
        #     print ("It is defined and has a value")


        # Get base url value
        # print()
        # print(self.subdomainPathentry.get())


        # scanSite = Scrapper("https://jobs.sanctuary-group.co.uk")
        # scanSite.init_page_scan('//ul[@class="pagination"]/li/a/@href', '/search')
        # # print(scanSite.get_pagination_list())

        # queryExpression = ['//table[@id="searchresults"]/tbody/tr', './td/span/a/text() | ./td/span/a/@href | ./td[@headers="hdrDepartment"]/span/text() | ./td/div/span/a/text() | ./td/div/span/span/text()']
        # scanSite.get_web_content('temp.txt', 'cleanTemp.txt', queryExpression, '/search/')

        # scanSite.get_url_list('cleanTemp.txt', 0)

        # queryExpressionTwo = ['//div[@id="innershell"]/div/div/div[@class="jobDisplayShell"]/div/div/div[@class="job"]', './div/div/div/div/h1/span[@itemprop="title"]/text() | ./div/div/div/div/span[@itemprop="jobLocation"]/p/span/text()']
        # scanSite.get_web_content('scrap.txt', 'cleanScrap.txt', queryExpressionTwo)
        # # scanSite.get_site_robot_txt()

        # for i in self.storeFormInputs.items():
        #     print(i.getFormUrl())
        #     print(i.getFormFilePath())
        #     print(i.getFormRow())
        #     print(i.getFormColumn())

        # Get values from instances
        # print(self.storeFormInputs[0].getFormUrl())
        # print(self.storeFormInputs[0].getFormFilePath())
        # print(self.storeFormInputs[0].getFormRow())
        # print(self.storeFormInputs[0].getFormColumn())

        # print(self.storeFormInputs[1].getFormUrl())
        # print(self.storeFormInputs[1].getFormFilePath())
        # print(self.storeFormInputs[1].getFormRow())
        # print(self.storeFormInputs[1].getFormColumn())

root = tk.Tk()
root.title("Web Scrapper")
root.geometry("1280x800")
app = MainUi(master=root)
app.mainloop()