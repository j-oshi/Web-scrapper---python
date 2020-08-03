from scrapper import Scrapper
import urllib.request
from lxml import etree, html

class SinglePage(Scrapper): 
    instances = []
    def __init__(self, name, url, subDomain, fileName, row, column):
        self.name = name
        self.url = url
        self.subDomain = subDomain
        self.fileName = fileName
        self.rowExpression = row
        self.columnExpression = column
        self.__class__.instances.append(self)
    
    def get_web_content(self):
        try:
            url = self.url + self.subDomain
            respData = self.get_html_content(url)

            queryContent = self.get_query_list(respData, self.rowExpression, self.columnExpression)
            file_name = self.name.replace(' ', '_') + '.txt'
            self.save_to_file(file_name, queryContent)
            # # Get pagination link list
            # paginationNodes = self.pagination_list(respData, queryExpression)

            # # Save unique list
            # self.paginationQueryList = self.ordered_set(paginationNodes)
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

    @classmethod
    def printIntances(cls):
        for instance in cls.instances:
            print(instance.propName())
