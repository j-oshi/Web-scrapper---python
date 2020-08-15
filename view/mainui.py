import sys
sys.path.append('D:/python-project/Web-scrapper---python/scrapper/')

import tkinter as tk
import tkinter.ttk as ttk
from searchWidget import SearchWidget
from scrapperFactory import ScrapperFactory

class MainUi(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.numberOfSearchWidgets = 0
        self.storeValue = {}
        self.storeChildValue = {}

        self.__createStyle()
        self.__createWIdget()
        self.__title()
        self.__add_widgets_control()
        self.__add_widgets_content()
        self.__submit()
        self.__hide_submit()
        self.__display_result()

    def __createStyle(self):
        self.s = ttk.Style()
        self.s.configure('App.TButton', background='#C0C0C0', foreground='#2b2d2f', font=(None, 12), padding=5)

    def __createWIdget(self):
        self.master.title("Web Scrapper")
        self.frame = tk.Frame(master=self.master, bg='#2b2d2f')
        self.frame.pack(fill=tk.BOTH, expand=True)

    def __title(self):
        self.titleframe = tk.Frame(master=self.frame, bg='#C0C0C0', padx=10, pady=10)
        self.titleframe.pack(fill=tk.X)

        self.titlelabel = tk.Label(master=self.titleframe, text='Web Scrapper', bg='#C0C0C0', font=(None, 16))
        self.titlelabel.pack()

    def __add_widgets_control(self):
        self.innerframe = tk.Frame(master=self.frame, bg='#2b2d2f', padx=10, pady=20)
        self.innerframe.pack(fill=tk.X)

        self.addWidgetLabel = tk.Label(
            master=self.innerframe,
            text='Run single or multipage page scrapper: ',
            bg='#2b2d2f',
            fg='#C0C0C0',
            padx=10, 
            font=(None, 12)
        )
        self.addWidgetLabel.pack(side='left')

        self.addWidgetButton = ttk.Button(
            master=self.innerframe,
            style='App.TButton'
        )
        self.addWidgetButton['text'] = 'Add scrapper'
        self.addWidgetButton["command"] = self.addwidgets
        self.addWidgetButton.pack(side='left')

    def __add_widgets_content(self):
        self.add_content_frame = tk.Frame(master=self.frame, bg='#2b2d2f', padx=20, pady=0)
        self.add_content_frame.pack(fill=tk.X)  

    def addwidgets(self):
        value = self.numberOfSearchWidgets
        if value < 3:
            SearchWidget(self.add_content_frame, self)
            self.numberOfSearchWidgets += 1      

    def __hide_submit(self):
        self.submitButton.pack_forget()

    def __submit(self):
        self.submitFrame = tk.Frame(master=self.frame, bg='#2b2d2f', padx=10, pady=20)
        self.submitFrame.pack(fill=tk.X)

        self.submitButton = ttk.Button(
            master=self.submitFrame,
            style='App.TButton'
        )
        self.submitButton['text'] = 'Run scrapper'
        self.submitButton["command"] = self.runProcess
        self.submitButton.pack()
    
    def __display_result(self):
        self.displayLabel = tk.Label(master=self.frame, text='', anchor='w', bg='#ffffff', font=(None, 12), padx=10, pady=10)
        self.displayLabel.pack(fill=tk.X)

    def runProcess(self):
        scrappers = self.storeValue
        for key, scrapper in scrappers.items():
            scrapper_factory = ScrapperFactory()
            scrapObj = scrapper_factory.create_scrapper(key, scrapper, self)
            scrapObj.web_content()
            self.storeChildValue.update(scrapObj.get_result())
            # self.displayLabel.destroy()
            # self.displayLabel.config(text="Internet is online")

root = tk.Tk()
root.geometry("1240x740")
app = MainUi(master=root)
app.mainloop()