from scrapper import Scrapper
import urllib.request
from lxml import html

import sys
sys.path.append('D:/python-project/Web-scrapper---python/helpers/')

from helper import getChildXpath, ordered_set
class SinglePage(Scrapper): 
    instances = []
    def __init__(self, name, scrapperData):
        self.name = name
        self.url = scrapperData.get('url')
        self.subDomain= scrapperData.get('subUrl')
        self.fileName = scrapperData.get('file')
        self.primaryExpression = scrapperData.get('row_search')
        self.secondaryExpression = scrapperData.get('column_search')

        self.storedResult = {}
        self.__class__.instances.append(self)

    def url_address(self): 
        return self.url + self.subDomain

    def header(self): 
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
        return headers

    def get_web_content(self):
        try:
            url = self.url_address()
            headers = self.header()

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
                    xpathResult = getChildXpath(item, secondaryXpath)
                    resultList.append(xpathResult)                   
            unique_data = resultList if not secondaryXpath else list(ordered_set(tuple(x) for x in resultList))
            print(unique_data)

            # save to fie
            if self.fileName:
                self.save_to_file(self.fileName, unique_data)
            else:
                file_name = self.name.replace(' ', '_') + '.txt'
                self.save_to_file(file_name, unique_data)

        except Exception as e:
            print(str(e)) 

    def save_to_file(self, filename, data):
        saveFile = open(filename, "w")
        saveFile.write(str(data))
        saveFile.write('\n')
        saveFile.close() 

    # def get_result(self):
    #     return self.storedResult

    # def test_run(self):
    #     try:
    #         f = open('test1.txt', "r")
    #         file = f.read() 

    #         queryContent = self.get_query_list(file, self.rowExpression, self.columnExpression)
    #         self.storedResult = queryContent

    #         # save to fie
    #         file_name = self.name.replace(' ', '_') + '.txt'
    #         self.save_to_file('test2', queryContent)
            
    #     except Exception as e:
    #         print(str(e)) 

    @classmethod
    def printIntances(cls):
        for instance in cls.instances:
            print(instance.propName())
