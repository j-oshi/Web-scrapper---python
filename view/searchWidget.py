import tkinter as tk
import tkinter.ttk as ttk


class SearchWidget:
    searchwidget = 1

    def __init__(self, master, parent):
        self.master = master
        self.parent = parent
        self.title="Scrapper " + str(SearchWidget.searchwidget)
        # self.url = ''
        # self.filepath = ''
        # self.row = ''
        # self.column = ''
        self.__createMiniStyle()
        self.__widget_container()
        self.__widget_title()
        self.__widget_base_content()
        self.__widget_subdomain_content()
        self.__widget_submit()
        # self.widget_label()
        # self.widget_base_content()
        # self.widget_base_url()
        # self.widget_subbase_content()
        # self.widget_subbase_url()
        # self.widget_search()
        # self.widget_row_search()
        # self.widget_column_search()
        # self.remove_button()
        # self.widget_subdomain_url()
        SearchWidget.searchwidget += 1

    def __createMiniStyle(self):
        self.s = ttk.Style()
        self.s.configure("ws.TFrame", background="#2b2d2f", padding=10, border=100)
        self.s.configure(
            "ws.TLabel",
            background="#2b2d2f",
            foreground="#C0C0C0",
            font=(None, 13),
            padding=10,
        )
        self.s.configure(
            "ur.TLabel",
            background="#2b2d2f",
            foreground="#C0C0C0",
            font=(None, 13),
            padding=10,
        )
        self.s.configure("ur.TEntry", foreground="#2b2d2f", padding=10)
        self.s.configure(
            "sur.TLabel",
            background="#2b2d2f",
            foreground="#C0C0C0",
            font=(None, 13),
            padding=10,
        )
        self.s.configure("sur.TEntry", foreground="#2b2d2f", padding=10)
        self.s.configure('sub.TButton', font=(None, 12), padding=5)

    def __widget_container(self):
        self.formName = ttk.Frame(
            master=self.master, relief=tk.RIDGE, borderwidth=5, style="ws.TFrame"
        )
        self.formName.pack(side="left")

    def __widget_title(self):
        self.formlabel = ttk.Label(
            master=self.formName,
            text=self.title,
            style="ws.TLabel",
        )
        self.formlabel.pack()

    def __widget_base_content(self):
        self.formContent = tk.Frame(master=self.formName,)
        self.formContent.pack()

        self.baseurllabel = ttk.Label(
            master=self.formContent, text="Base url: ", style="ur.TLabel"
        )
        self.baseurllabel.pack(side="left")

        # Search url entry
        self.url = ttk.Entry(master=self.formContent, style="ur.TEntry")
        self.url.pack(side="left")

    def __widget_subdomain_content(self):
        self.formSubUrl = tk.Frame(master=self.formName,)
        self.formSubUrl.pack()

        self.subUrllabel = ttk.Label(
            master=self.formSubUrl, text="Sub Domian url: ", style="sur.TLabel"
        )
        self.subUrllabel.pack(side="left")

        # Search url entry
        self.subUrl = ttk.Entry(master=self.formSubUrl, style="ur.TEntry")
        self.subUrl.pack(side="left")

    def __widget_submit(self):
        self.subSubmitFrame = ttk.Frame(master=self.formName, style="s.TFrame")
        self.subSubmitFrame.pack(fill=tk.X)

        self.subSubmitButton = ttk.Button(
            master=self.subSubmitFrame, style="sub.TButton"
        )

        self.subSubmitButton["text"] = "Add to process"
        self.subSubmitButton["command"] = self.getValue
        self.subSubmitButton.pack(side="left")

        self.rsubSubmitButton = ttk.Button(
            master=self.subSubmitFrame, style="sub.TButton"
        )

        self.rsubSubmitButton["text"] = "Remove from process"
        self.rsubSubmitButton["command"] = self.removeValue
        self.rsubSubmitButton.pack(side="left")

    def getValue(self):
        dict = {}
        key = self.title
        url = self.url.get()
        subUrl = self.subUrl.get()
        dict[key] = {'url': url, 'subUrl': subUrl}
        self.parent.storeValue.update(dict)

    def removeValue(self):
        dict = {}
        key = self.title
        url = self.url.get()
        subUrl = self.subUrl.get()
        dict[key] = {'url': url, 'subUrl': subUrl}
        self.parent.storeValue.update(dict)

    # def widget_subbase_content(self):
    #     self.search_subcontent = tk.Frame(
    #         master=self.formName,
    #         bg="#2b2d2f",
    #         padx=10,
    #         pady=10
    #     )
    #     self.search_subcontent.pack()

    # def widget_subbase_url(self):
    #     self.subdomainurllabel = tk.Label(
    #         master=self.search_subcontent,
    #         text=f"Sub domain: ",
    #         font=(None, 12),
    #         fg="#C0C0C0",
    #         bg="#2b2d2f",
    #     )
    #     self.subdomainurllabel.grid(row = 0, sticky = W)

    #     # Search url entry
    #     self.suburl = tk.Entry(master=self.search_subcontent)
    #     self.suburl.grid(row=0, column=1)

    # def widget_search(self):
    #     self.search = tk.Frame(
    #         master=self.formName,
    #         bg="#2b2d2f",
    #         padx=10,
    #         pady=10
    #     )
    #     self.search.pack()

    # def widget_row_search(self):
    #     self.rowurllabel = tk.Label(
    #         master=self.search,
    #         text=f"Row search: ",
    #         font=(None, 12),
    #         fg="#C0C0C0",
    #         bg="#2b2d2f",
    #         padx=10,
    #         pady=10
    #     )
    #     self.rowurllabel.grid(row=0, column=0)

    #     # Search url entry
    #     self.row = tk.Entry(master=self.search, width=55)
    #     self.row.grid(row=1, column=0, columnspan=2)

    # def widget_column_search(self):
    #     self.columnlabel = tk.Label(
    #         master=self.search,
    #         text=f"Column expressions",
    #         font=(None, 12),
    #         padx=10,
    #         pady=10,
    #         fg="#C0C0C0",
    #         bg="#2b2d2f",
    #     )
    #     self.columnlabel.grid(row=2, column=0)

    #     # Column expressions entry
    #     self.column = tk.Text(master=self.search, width=45, height = 10)
    #     self.column.grid(row=3, column=0)

    # def remove_button(self):
    #     self.removesearch = tk.Button(
    #         master=self.formName, font=(None, 13), padx=5, pady=5
    #     )
    #     self.removesearch["text"] = "Remove widget"
    #     self.removesearch["command"] = self.removeWidget
    #     self.removesearch.pack()

    # def removeWidget(self):
    #     self.formName.pack_forget()
    #     self.formName.destroy()
    #     if self.parent.numberOfSearchWidgets > 0:
    #         self.parent.numberOfSearchWidgets = self.parent.numberOfSearchWidgets - 1



    # def getFormUrl(self):
    #     url = self.url.get()
    #     return url

    # def getFormFilePath(self):
    #     filepath = self.filepath.get()
    #     return filepath

    # def getFormRow(self):
    #     row = self.row.get()
    #     return row

    # def getFormColumn(self):
    #     column = self.column.get("1.0", tk.END)
    #     return column
