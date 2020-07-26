import urllib.request
from lxml import etree
from io import StringIO
from collections import ChainMap
import ast
import itertools

class Scrapper:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        self.pageContent = ''
        self.paginationQueryList = []
        self.siteData = dict()

    # Check header status response
    # def validate_url(self):
        # request = urllib.request.urlopen('https://www.asda.com')
        # # print(request.getheaders())
        # print(request.getheader('Content-Disposition'))
        # if request.status_code == 200:
        #     print('Web site exists')
        # else:
        #     print('Web site does not exist')
        # conn = http.client.HTTPSConnection(self.url)
        # conn.request("HEAD", "")
        # value = True
        # if conn.getresponse().status == 200:
        #     return value
    def page_html_content(self, url):
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        return resp.read()

    def init_page_scan(self, saveToFile, queryExpression, urlPath=''):
        try:
            url = self.baseUrl + urlPath

            respData = self.page_html_content(url)
            self.pageContent = respData
            paginationNodes = self.pagination_list(respData, queryExpression)

            # Get the url from the ref
            queryList = []
            for el in paginationNodes:
                queryList.append(el.get('href', ''))
            # Save unique list
            self.paginationQueryList = self.ordered_set(queryList)
        except Exception as e:
            print(str(e))

    def get_web_content(self, saveToFile, queryExpression, urlPath=''):
        try:
            queryList = []
            queryList = self.paginationQueryList
            if len(queryList) > 0:
                url = self.baseUrl

                chain_map = ChainMap()
                open(saveToFile, 'w').close()

                for queryString in queryList:
                    queryUrl = url + urlPath + queryString
                    respData = self.page_html_content(queryUrl)
                    siteNodes = self.parse_html(respData, queryExpression)
                     
                    for el in siteNodes:
                        test = el.xpath('//span[@class="jobTitle hidden-phone"]/a')
                        counter = 0
                        example = {}                   
                        for e in test:
                            example.setdefault(counter, {})['title']=e.text
                            example.setdefault(counter, {})['href']=e.get('href', '')
                            counter = counter + 1 
                        data = example
                        new_chain_map = chain_map.new_child(data)

                    saveFile = open(saveToFile, "a+")

                    # for element in new_chain_map:
                    saveFile.write(str(new_chain_map.maps))
                    saveFile.write('\n')
                    saveFile.close()     

                # Get content in temp file and clean              
                self.cleanList(saveToFile)
                    # print("%s => %s" % (e.tag, e.text))
                    # print(e.xpath('//span/a'))
                    # etree.dump(e)

                # for element in urlList:
                #     saveFile.write(element)
                #     saveFile.write('\n')
                # saveFile.close()

        except Exception as e:
            print(str(e))

    # Clean list in temp file and save to another file
    def cleanList(self, filename):
        f = open(filename, "r")
        file = f.read() 
        li = list(file.replace('}',' {').split("{"))
        result = []
        for s in li:
            if 'title' in s:
                result.append(s)
        
        saveFile = open('scrap.txt', "w")
        # for element in new_chain_map:
        saveFile.write(str(result))
        saveFile.write('\n')
        saveFile.close()    

    def pagination_list(self, htmlcontent, queryExpression):
        nodes = self.parse_html(htmlcontent, queryExpression)
        return nodes

    def parse_html(self, htmlcontent, queryExpression):
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO(str(htmlcontent)), parser=parser)
        nodes = tree.xpath(queryExpression)
        return nodes

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

    # Read site robot.txt
    def get_site_robot_txt(self):
        # stream = urllib.request.urlopen(self.url + "/robots.txt")
        stream = urllib.request.urlopen(
            "https://jobs.sanctuary-group.co.uk/robots.txt")
        print(stream.read().decode("utf-8"))

    def get_pagination_list(self):
        return self.paginationQueryList

    def get_page_content(self):
        return self.pageContent


scanSite = Scrapper("https://jobs.sanctuary-group.co.uk")
scanSite.init_page_scan('test4.txt', '//ul[@class="pagination"]/li/a', '/search')
scanSite.get_web_content('temp.txt', '//table[@id="searchresults"]/tbody/tr/td', '/search/')


# print(scanSite.get_pagination_list())
# print(scanSite.get_page_content())
# scanSite.get_site_robot_txt()
