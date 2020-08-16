import urllib.request
from lxml import etree, html

class Scrapper:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        self.pageContent = ''
        self.paginationQueryList = []

    # Scan for pagination and get links.
    def init_page_scan(self, queryExpression, urlPath=''):
        try:
            url = self.baseUrl + urlPath
            respData = self.page_html_content(url)

            # Get pagination link list
            paginationNodes = self.pagination_list(respData, queryExpression)

            # Save unique list
            self.paginationQueryList = self.ordered_set(paginationNodes)
        except Exception as e:
            print(str(e))

    # Get node content per link
    def get_web_content(self, saveToFile, cleanTemp, queryExpression, urlPath=''):
        try:
            queryList = []
            queryList = self.paginationQueryList
            if len(queryList) > 0:
                url = self.baseUrl

                open(saveToFile, 'w').close()

                for queryString in queryList:
                    queryUrl = url + urlPath + queryString
                    respData = self.page_html_content(queryUrl)
                    root = self.parse_html(respData, queryExpression[0])

                    data = []
                    for row in root:
                        test = row.xpath(queryExpression[1])
                        data.append(test)

                    saveFile = open(saveToFile, "a+")
                    # for element in new_chain_map:
                    saveFile.write(str(data))
                    saveFile.write('\n')
                    saveFile.close()     

                # Get content in temp file and clean              
                self.cleanList(saveToFile, cleanTemp)
                    # print("%s => %s" % (e.tag, e.text))
                    # print(e.xpath('//span/a'))
                    # etree.dump(e)

        except Exception as e:
            print(str(e))

    def page_html_content(self, url):
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        return resp.read()

    # Clean list in temp file and save to another file
    def cleanList(self, filename, distFile):
        f = open(filename, "r")
        file = f.read() 
        result = file.replace('[[','[').replace(']]','],')
        saveFile = open(distFile, "w")
        # for element in new_chain_map:
        saveFile.write(str(result))
        saveFile.write('\n')
        saveFile.close()  

    def pagination_list(self, htmlcontent, queryExpression):
        nodes = self.parse_html(htmlcontent, queryExpression)
        return nodes

    def parse_html(self, htmlcontent, queryExpression):
        tree = html.fromstring(htmlcontent)
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

    def get_url_list(self, filename, columnPosition):
        f = open(filename, "r")
        file = f.read() 
        result = file.replace(']',']]').split('],')
        queryList = []
        for i in result:
            row = i.replace('[','').replace(']','').replace("'","").replace(" ","").split(',')
            column = row[columnPosition]
            if column != '\n\n':
              queryList.append(column.strip())
        self.paginationQueryList = queryList

    def get_page_content(self):
        return self.pageContent


scanSite = Scrapper("https://jobs.sanctuary-group.co.uk")
scanSite.init_page_scan('//ul[@class="pagination"]/li/a/@href', '/search')
# print(scanSite.get_pagination_list())

queryExpression = ['//table[@id="searchresults"]/tbody/tr', './td/span/a/text() | ./td/span/a/@href | ./td[@headers="hdrDepartment"]/span/text() | ./td/div/span/a/text() | ./td/div/span/span/text()']
scanSite.get_web_content('temp.txt', 'cleanTemp.txt', queryExpression, '/search/')

scanSite.get_url_list('cleanTemp.txt', 0)

queryExpressionTwo = ['//div[@id="innershell"]/div/div/div[@class="jobDisplayShell"]/div/div/div[@class="job"]', './div/div/div/div/h1/span[@itemprop="title"]/text() | ./div/div/div/div/span[@itemprop="jobLocation"]/p/span/text()']
scanSite.get_web_content('scrap.txt', 'cleanScrap.txt', queryExpressionTwo)
# scanSite.get_site_robot_txt()
