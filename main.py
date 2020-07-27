import tkinter as tk
from scrapper import Scrapper

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_scrapper_widgets()

    def create_scrapper_widgets(self):
        self.si = tk.Button(self)
        self.si["text"] = "Scrap site\n(click me)"
        self.si["command"] = self.runScrapper
        self.si.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def runScrapper(self):
        scanSite = Scrapper("https://jobs.sanctuary-group.co.uk/search/")
        scanSite.get_web_content('test2.txt')
        # print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()