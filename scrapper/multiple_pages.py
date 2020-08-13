from page_scrapper import PageScrapper
class MultiPage(PageScrapper):
    instances = []
    def __init__(self, name, scrapperData, parent):
        super().__init__(name, scrapperData)
        self.__class__.instances.append(self)
        self.parent = parent
        self.storeValue = {}

    def get_name(self):
        return self.name

    def __filename(self):
        return super()._filename()

    def web_content(self):
        connectTo = super()._connectTo()
        objName = self.get_name()
        if connectTo:
            urlList = self.parent.storeChildValue.get(connectTo)
            a_list = []
            for item in urlList:
                url = super()._url_address() + item
                scrap_data = super().get_web_content(url)
                a_list.append(scrap_data)

            self.storeValue[objName] = a_list
        else:
            url = super()._url_address()
            scrap_data = super().get_web_content(url)

            self.storeValue[objName] = scrap_data  

        # save to fie
        if self._filename():
            super().save_to_file(self._filename(), self.storeValue)
        else:
            file_name = self.get_name().replace(' ', '_') + '.txt'
            super().save_to_file(file_name, self.storeValue)

    def get_result(self):
       return {'Scrapper 2': self.parent.storeChildValue}

    @classmethod
    def printIntances(cls):
        for instance in cls.instances:
            print(instance.propName())
