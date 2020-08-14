from page_scrapper import PageScrapper

class MultiPage(PageScrapper):
    instances = []
    def __init__(self, name, scrapperData, parent):
        super().__init__(name, scrapperData)
        self.__class__.instances.append(self)
        self.parent = parent
        self.storeInstanceValue = {}

    def get_name(self):
        return self.name

    def __filename(self):
        return super()._filename()

    def web_content(self):
        connectTo = super()._connectTo()
        objName = self.get_name()
        self.storeInstanceValue.clear()
        if connectTo:
            urlList = self.parent.storeChildValue.get(connectTo)
            if any( isinstance(e, list) for e in urlList ):
                flat_list = [item for sublist in urlList for item in sublist]
            else:
                flat_list = urlList

            a_list = []
            for item in flat_list:
                url = super()._url_address() + item
                scrap_data = super().get_web_content(url)
                a_list.append(scrap_data)

            self.storeInstanceValue[objName] = a_list
        else:
            url = super()._url_address()
            scrap_data = super().get_web_content(url)

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
