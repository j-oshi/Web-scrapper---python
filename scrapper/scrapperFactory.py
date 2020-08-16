from .single_page import SinglePage
from .multiple_pages import MultiPage

class ScrapperFactory():
    def create_scrapper(self, scrapperName, scrapperData, parent):
        scrapperType = scrapperData.get('type').strip().lower()
        if scrapperType == 'single':
            return SinglePage(scrapperName, scrapperData)
        elif scrapperType == 'multiple':
            return MultiPage(scrapperName, scrapperData, parent)