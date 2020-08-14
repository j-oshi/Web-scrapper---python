from scrapper import Scrapper
import urllib.request
from lxml import html

class PageScrapper(Scrapper): 
    def __init__(self, name, scrapperData):
        self.name = name
        self.url = scrapperData.get('url')
        self.subDomain= scrapperData.get('subUrl')
        self.fileName = scrapperData.get('file')
        self.connectTo = scrapperData.get('connectTo')
        self.primaryExpression = scrapperData.get('row_search')
        self.secondaryExpression = scrapperData.get('column_search')

        self.storedResult = {}
    
    def _filename(self): 
        return self.fileName

    def _url_address(self): 
        return self.url + self.subDomain

    def _connectTo(self): 
        return self.connectTo

    def _header(self): 
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
        return headers

    def get_web_content(self, url):
        try:
            headers = self._header()

            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            tree = html.fromstring(resp.read())

            primaryXpath = self.primaryExpression.strip()
            primaryData = tree.xpath(primaryXpath)
            
            secondaryXpath = self.secondaryExpression.strip().splitlines()

            resultList = [] 
            mmap = {}
  
            for item in primaryData:
                if not secondaryXpath: 
                    if item not in mmap:
                        mmap[item] = 1
                        resultList.append(item)
                else:
                    xpathResult = self.getChildXpath(item, secondaryXpath)
                    resultList.append(xpathResult)                   
            unique_data = resultList if not secondaryXpath else list(self.ordered_set(tuple(x) for x in resultList))
            return unique_data

        except Exception as e:
            print(str(e)) 

    def save_to_file(self, filename, data):
        fileLocation = '../data/'
        saveFile = open(fileLocation + filename, "w")
        saveFile.write(str(data))
        saveFile.write('\n')
        saveFile.close() 

    def getChildXpath(self, xpathObj, listObj):
        x = []
        for i in listObj:
            x.append(xpathObj.xpath(i))
        all_lists = sum(x, [])
        return all_lists
        
    def ordered_set(self, alist):
        # Creates an ordered set of unique items
        mmap = {}  # implements hashed lookup
        oset = []  # storage for set

        for item in alist:
        # Save unique items in input order
            if item not in mmap:
                mmap[item] = 1
                oset.append(item)
        return oset
