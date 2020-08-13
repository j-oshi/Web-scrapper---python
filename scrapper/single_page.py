from page_scrapper import PageScrapper
class SinglePage(PageScrapper): 
    instances = []
    def __init__(self, name, scrapperData):
        super().__init__(name, scrapperData)
        self.__class__.instances.append(self)
        self.storeValue = {}
    
    def get_name(self):
        return self.name

    def __filename(self):
        return super()._filename()

    def web_content(self):
        url = super()._url_address()
        scrap_data = super().get_web_content(url)

        objName = self.get_name()
        self.storeValue[objName] = scrap_data

        # save to fie
        if self._filename():
            super().save_to_file(self._filename(), scrap_data)
        else:
            file_name = self.get_name().replace(' ', '_') + '.txt'
            super().save_to_file(file_name, scrap_data)

    def get_result(self):
        return self.storeValue

    @classmethod
    def printIntances(cls):
        for instance in cls.instances:
            print(instance.propName())