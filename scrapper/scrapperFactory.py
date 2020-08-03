from single_page import SinglePage
from multiple_pages import MultiPage

class ScrapperFactory():
    def create_scrapper(self, scrapperName, scrapperData):
        scrapperType = scrapperData['type'].strip().lower()
        url = scrapperData['url']
        sub_url = scrapperData['subUrl']
        fileName = scrapperData['file']
        connectTo = scrapperData['connectTo']
        row = scrapperData['row_search']
        column = scrapperData['column_search']

        if scrapperType == 'single':
            return SinglePage(scrapperName, url, sub_url, fileName, row, column)
            # print(scrapperName + ' factory is active' + scrapperData['type'])
        elif scrapperType == 'muliple':
            print('yes sir')