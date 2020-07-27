import urllib.request
from lxml import etree, html
from io import StringIO

class XpathFinder:
    def __init__(self, expression):
        self.expression = expression

    # def scanTree(self):
        # headers = {}
        # headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
        # req = urllib.request.Request('https://jobs.sanctuary-group.co.uk/search', headers=headers)
        # resp = urllib.request.urlopen(req)
        # saveFile = open('test2.txt', "w")
        # saveFile.write(resp)
        # saveFile.close()   
        # file = saveFile.read()
        # return file
#         with open("text2.txt", "r", encoding='utf-8') as f:
#             page = f.read()
#             tree = html.fromstring(page)
#             root = tree.xpath('//table[@id="searchresults"]/tbody/tr')
#             data = []
#             for row in root:
#                 test = row.xpath('./td/span/a/text() | ./td/span/a/@href | ./td[@headers="hdrDepartment"]/span/text() | ./td/div/span/a/text() | ./td/div/span/span/text()')
#                 data.append(test)
#             print(data)

# testaa = XpathFinder('test')
# testaa.scanTree()