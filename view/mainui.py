import sys
sys.path.append('D:/python-project/Web-scrapper---python/scrapper/')

import tkinter as tk
import tkinter.ttk as ttk
from searchWidget import SearchWidget
from scrapperFactory import ScrapperFactory
# from scrapper import Scrapper

class MainUi(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.numberOfSearchWidgets = 0
        self.storeValue = {}

        self.__createStyle()
        self.__createWIdget()
        self.__title()
        self.__add_widgets_control()
        self.__add_widgets_content()
        self.__submit()
        self.__hide_submit()

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

    def runProcess(self):
        scrappers = self.storeValue
        for key, scrapper in scrappers.items():
            print(scrapper)
            scrapper_factory = ScrapperFactory()
            scrapObj = scrapper_factory.create_scrapper(key, scrapper)
            scrapObj.get_web_content()
            # print(scrapObj.get_result())
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
root.geometry("1300x800")
app = MainUi(master=root)
app.mainloop()