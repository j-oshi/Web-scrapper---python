import tkinter as tk
import tkinter.ttk as ttk

class SearchWidget:
    searchwidget = 1

    def __init__(self, master, parent):
        self.master = master
        self.parent = parent
        self.title = "Scrapper " + str(SearchWidget.searchwidget)

        self.__createMiniStyle()
        self.__widget_container()
        self.__widget_title()
        self.__widget_select()
        self.__widget_base_content()
        self.__widget_subdomain_content()
        self.__widget_output_content()
        self.__widget_row_search()
        self.__widget_column_search()
        self.__hide_connect_to()
        self.__widget_submit()
        self.__hide_process()

        SearchWidget.searchwidget += 1

    def __createMiniStyle(self):
        self.s = ttk.Style()
        self.s.configure("ws.TFrame", background="#2b2d2f", padding=10)

    def __widget_container(self):
        self.formName = tk.Frame(
            master=self.master, relief=tk.RIDGE, bg='#2b2d2f', borderwidth=5, padx=10, pady=10
        )
        self.formName.pack(side="left")

    def __widget_title(self):
        self.formlabel = tk.Label(
            master=self.formName,
            text=self.title,
            bg='#2b2d2f',
            fg='#C0C0C0',
            font=(None, 12), 
            pady=10
        )
        self.formlabel.pack(fill=tk.X)

    def __widget_select(self):
        self.frameOne = tk.Frame(master=self.formName, bg='#2b2d2f')
        self.frameOne.pack(fill=tk.X)

        self.comboLabel = tk.Label(self.frameOne, font=(None, 10), text="Select type: ", bg='#2b2d2f', fg='#C0C0C0', width=15, pady=5)
        self.comboLabel.grid(column=0, row=0)

        n = tk.StringVar()
        self.comboSelect = ttk.Combobox(self.frameOne, width=37, textvariable=n)
        self.comboSelect['values'] = (' Single', ' Multiple')
        self.comboSelect.grid(column=1, row=0)
        self.comboSelect.current()
        self.comboSelect.bind("<<ComboboxSelected>>", self.onselectConnectChange)

    def __widget_base_content(self):
        self.frameTwo = tk.Frame(master=self.formName, bg='#2b2d2f')
        self.frameTwo.pack(fill=tk.X)

        self.baseurllabel = tk.Label(master=self.frameTwo, font=(None, 10), text="Base url: ", bg='#2b2d2f', fg='#C0C0C0', width=15, pady=5)
        self.baseurllabel.pack(side="left")

        self.url = tk.Entry(master=self.frameTwo, width=40)
        self.url.pack(side="left", expand=1)

    def __widget_subdomain_content(self):
        self.frameThree = tk.Frame(master=self.formName, bg='#2b2d2f')
        self.frameThree.pack(fill=tk.X)

        self.suburllabel = tk.Label(master=self.frameThree, font=(None, 10), text="Sub domain url: ", bg='#2b2d2f', fg='#C0C0C0', width=15, pady=5)
        self.suburllabel.pack(side="left")
        self.suburl = tk.Entry(master=self.frameThree, width=40)
        self.suburl.pack(side="left", expand=1)

    def __widget_output_content(self):
        self.frameInner = tk.Frame(master=self.formName, borderwidth=0, bg='#2b2d2f')
        self.frameInner.pack(fill=tk.X)

        self.frameFour = tk.Frame(master=self.frameInner, bg='#2b2d2f')
        self.frameFour.pack(fill=tk.X)

        self.outputlabel = tk.Label(master=self.frameFour, font=(None, 10), text="Output to: ", bg='#2b2d2f', fg='#C0C0C0', width=15, pady=5)
        self.outputlabel.pack(side="left")
        self.output = tk.Entry(master=self.frameFour, width=40)
        self.output.pack(side="left", expand=1)

        self.frameFive = tk.Frame(master=self.frameInner, bg='#2b2d2f')
        self.frameFive.pack(fill=tk.X)

        self.connectLabel = tk.Label(master=self.frameFive, font=(None, 10), text="Connect to: ", bg='#2b2d2f', fg='#C0C0C0', width=15, pady=5)
        self.connectLabel.grid(column=0, row=0)

        n = tk.StringVar()
        self.connectSelect = ttk.Combobox(master=self.frameFive, width=37, textvariable=n)
        # self.connectSelect["command"] = self.loadToselect
        for i in self.parent.storeValue:
            self.connectSelect['values'] = (i, )
        self.connectSelect.grid(column=1, row=0)
        self.connectSelect.current()

        self.frameFivetwo = tk.Frame(master=self.frameInner, bg='#2b2d2f')
        self.frameFivetwo.pack(fill=tk.X)

        # self.columnSelectLabel = tk.Label(master=self.frameFivetwo, font=(None, 10), text="List column: ", bg='#2b2d2f', fg='#C0C0C0', width=15, pady=5)
        # self.columnSelectLabel.pack(side="left")

        self.columnSelect = tk.Entry(master=self.frameFivetwo, width=10)
        self.columnSelect.pack(side="left", expand=1)

    def __widget_row_search(self):
        self.frameSix = tk.Frame(master=self.formName, bg='#2b2d2f')
        self.frameSix.pack(fill=tk.X)

        self.nodeSearchlabel = tk.Label(master=self.frameSix, font=(None, 10), text='Node search: ', bg='#2b2d2f', fg='#C0C0C0', width=15, pady=5)
        self.nodeSearchlabel.pack(side="left")

        self.nodeSearch = tk.Entry(master=self.frameSix, width=40)
        self.nodeSearch.pack(side="left", expand=1)

    def __widget_column_search(self):
        self.frameSeven = tk.Frame(master=self.formName, bg='#2b2d2f', pady=5)
        self.frameSeven.pack(fill=tk.X)

        self.fieldSearchlabel = tk.Label(master=self.frameSeven, font=(None, 10), text='Field search: ', bg='#2b2d2f', fg='#C0C0C0', width=15, pady=5)
        self.fieldSearchlabel.pack(side="left")
        self.fieldSearch = tk.Text(master=self.frameSeven, width=30, height = 10)
        self.fieldSearch.pack(side="left", expand=1)

    def __widget_submit(self):
        self.subSubmitFrame = tk.Frame(master=self.formName, bg='#2b2d2f', pady=10)
        self.subSubmitFrame.pack(fill=tk.X)

        self.subSubmitButton = tk.Button(
            master=self.subSubmitFrame, font=(None, 10), padx=5, pady=5, activebackground='green'
        )
        self.subSubmitButton["text"] = "Add to process"
        self.subSubmitButton["command"] = self.getValue
        self.subSubmitButton.pack()

        self.rsubSubmitButton = tk.Button(
            master=self.subSubmitFrame, font=(None, 10), padx=5, pady=5
        )
        self.rsubSubmitButton["text"] = "Remove from process"
        self.rsubSubmitButton["command"] = self.removeValue
        self.rsubSubmitButton.pack()

    def __hide_connect_to(self):
        self.frameFive.pack_forget()
        self.frameFivetwo.pack_forget()

    def __hide_process(self):
        self.subSubmitButton.pack_forget() 
        self.rsubSubmitButton.pack_forget() 

    def getValue(self):
        self.subSubmitButton.pack_forget() 
        dict = {}
        key = self.title
        scrapper_type = self.comboSelect.get()
        url = self.url.get()
        subUrl = self.suburl.get()
        file = self.output.get()
        connectTo =  self.connectSelect.get() if scrapper_type == ' Multiple' else ''
        column_select = self.columnSelect.get()
        row_search = self.nodeSearch.get()
        column_search = self.fieldSearch.get("1.0", tk.END)
        dict[key] = {'type': scrapper_type, 'url': url, 'subUrl': subUrl, 'file': file, 'connectTo': connectTo, 'column_select': column_select, 'row_search': row_search, 'column_search': column_search}
        self.formName.configure(background='green')
        self.parent.storeValue.update(dict)
        self.rsubSubmitButton.pack()
        if self.parent.numberOfSearchWidgets > 0: 
            self.parent.submitButton.pack() 
        # self.rsubSubmitButton.pack() 

    def removeValue(self):
        self.formName.pack_forget()
        self.formName.destroy()

        objKey = self.title

        # Remove instance
        if objKey in self.parent.storeValue: del self.parent.storeValue[objKey]

        if self.parent.numberOfSearchWidgets > 0:
            self.parent.numberOfSearchWidgets = self.parent.numberOfSearchWidgets - 1
            if self.parent.numberOfSearchWidgets < 1:
                self.parent.submitButton.pack_forget() 

    def onselectConnectChange(self, *args):
        switchOutput = self.comboSelect.get().strip().lower()
        self.subSubmitButton.pack()
        self.rsubSubmitButton.pack_forget()  
        if switchOutput == 'multiple':
            self.frameFive.pack() 
            self.formName.configure(background='orange')
            self.frameFivetwo.pack()
        else: 
            self.frameFive.pack_forget() 
            self.formName.configure(background='yellow')
            self.frameFivetwo.forget()
