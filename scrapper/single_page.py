from page_scrapper import PageScrapper
class SinglePage(PageScrapper): 
    instances = []
    def __init__(self, name, scrapperData):
        super().__init__(name, scrapperData)
        self.__class__.instances.append(self)
        self.storeInstanceValue = {}
    
    def get_name(self):
        return self.name

    def __filename(self):
        return super()._filename()

    def web_content(self):
        url = super()._url_address()
        scrap_data = super().get_web_content(url)

        objName = self.get_name()
        self.storeInstanceValue[objName] = scrap_data

        # save to fie
        if self._filename():
            super().save_to_file(self._filename(), self.storeInstanceValue)
        else:
            file_name = self.get_name().replace(' ', '_') + '.txt'
            super().save_to_file(file_name, self.storeInstanceValue)

    def get_result(self):
        return self.storeInstanceValue

    @classmethod
    def printIntances(cls):
        for instance in cls.instances:
            print(instance.propName())