from scrapper import Scrapper
import urllib.request
from lxml import etree, html

class SinglePage(Scrapper): 
    instances = []
    def __init__(self, name, scrapperData):
        self.name = name
        self.url = scrapperData.get('url')
        self.subDomain= scrapperData.get('subUrl')
        self.fileName = scrapperData.get('file')
        self.rowExpression = scrapperData.get('row_search')
        self.columnExpression = scrapperData.get('column_search')

        self.storedResult = {}
        self.__class__.instances.append(self)
    
    def get_web_content(self):
        try:
            url = self.url + self.subDomain
            respData = self.get_html_content(url)

            queryContent = self.get_query_list(respData, self.rowExpression, self.columnExpression)
            self.storedResult = queryContent

            # save to fie
            file_name = self.name.replace(' ', '_') + '.txt'
            self.save_to_file(file_name, queryContent)

        except Exception as e:
            print(str(e)) 

    def get_html_content(self, url):
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        return resp.read()

    def get_query_list(self, htmlcontent, rowExpression, columnExpression):
        tree = html.fromstring(htmlcontent)
        nodes = tree.xpath(rowExpression)
        return nodes

    def save_to_file(self, filename, data):
        saveFile = open(filename, "w")
        saveFile.write(str(data))
        saveFile.write('\n')
        saveFile.close() 

    def get_result(self):
        return self.storedResult

    def convert_to_sub_query_expressions(self):
        self.rowExpression      
        self.columnExpression
        pass

    def test_run(self):
        try:
            f = open('test1.txt', "r")
            file = f.read() 

            queryContent = self.get_query_list(file, self.rowExpression, self.columnExpression)
            self.storedResult = queryContent

            # save to fie
            file_name = self.name.replace(' ', '_') + '.txt'
            self.save_to_file('test2', queryContent)
            
        except Exception as e:
            print(str(e)) 

    @classmethod
    def printIntances(cls):
        for instance in cls.instances:
            print(instance.propName())
