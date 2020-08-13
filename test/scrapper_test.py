# import sys
# import json
# # print(sys.path)

# import urllib.request
# # from lxml import etree, html

# sys.path.append('D:/python-project/Web-scrapper---python/scrapper/')

# try:
#     url = 'http://oshinit.com/'

#     headers = {}
#     headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
#     req = urllib.request.Request(url, headers=headers)
#     resp = urllib.request.urlopen(req)
#     respData = resp.read()          
           
#     saveFile = open('test.txt', 'w')  
#     saveFile.write(str(respData)) 
#     saveFile.close()
#             # respData = self.page_html_content(url)

#             # Get pagination link list
#             # paginationNodes = self.pagination_list(respData, queryExpression)

#             # Save unique list
#             # self.paginationQueryList = self.ordered_set(paginationNodes)
# except Exception as e:
#             print(str(e))

# import re

# testring = '''In Giant-Size X-Men #1 (1975), writer Len Wein and artist Dave Cockrum introduced a new team that starred in a revival of The X-Men, beginning with issue #94. This new team replaced the previous members with the exception of Cyclops, who remained. This team differed greatly from the original. Unlike in the early issues of the original series, the new team was not made up of teenagers and they also had a more diverse background. Marvel's corporate owners, Cadence Industries, had suggested the new team should be international, feeling it needed characters with "foreign appeal".[8] So each character was from a different country with varying cultural and philosophical beliefs, and all were already well-versed in using their mutant powers, several being experienced in combat. Another major difference is that unlike the original X-Men who were White Anglo-Saxon Protestants (WASPs) with the exception of the half-Irish/half-Jewish Iceman, the "All-New, All-Different" X-Men team was composed of a Soviet/Russian atheist, a German Catholic blue demon-like creature, a female African Kenyan-American woman, an Irish Catholic, an Apache Native American, a Japanese male and a Canadian agent as its members.
# The "all-new, all-different X-Men"[9] were led by Cyclops, from the original team, and consisted of the newly created Colossus (from the Soviet Union/Russia), Nightcrawler (from West Germany/Germany), Storm (from Kenya), and Thunderbird (a Native American of Apache descent), and three previously introduced characters: Banshee (from Ireland), Sunfire (from Japan), and Wolverine (from Canada). Wolverine eventually became the breakout character on the team and, in terms of comic sales and appearances, the most popular X-Men character even getting his own solo title. Sunfire would reject membership of the X-men shortly after their first mission. However, this team would not remain whole for long as Sunfire quit immediately and never really accepted the other members, and Thunderbird would die in the very next mission. Filling in the vacancy, a revamped Jean Grey soon rejoined the X-Men under her new persona of "Phoenix". Angel, Beast, Iceman, Havok, and Polaris also made significant guest appearances. 
# '''
# print(re.search('\(', testring))  
# print(re.findall('\(\D+\)', testring)) 


# f = open('test.txt', "r")
# file = f.read() 
# hmtl = re.findall('<p>.*?</p>', file)
# allWord = re.findall('<p>.*?</p>', file)
# for match in allWord:
#     print(re.sub("<[^<>]+>", "", match))
# print() 
# html = re.sub('<[^<>]+>', '', file)
# print(html)
# hmtl = re.findall('<p>.*?</p>', file)
# print(re.findall('<p>.*?</p>', file)) 
# 
# print(file)

# p = re.compile(r'\D+')
# getMatchValue = p.findall(testring)

# print(getMatchValue)
# getMatch = re.compile('X-men*', re.IGNORECASE)

# getMatchValue = getMatch.findall(testring)
# # name = re.findall(r'[A-Z][a-z]*', testring)

# print(getMatchValue)
# p = re.compile('drum')
# iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
# for match in iterator:
#     print(match.span())

# from lxml import etree

# def innerXML(elem):
#     elemName = elem.xpath('name(/*)')
#     resultStr = ''
#     for e in elem.xpath('/'+ elemName + '/node()'):
#         if(isinstance(e, str) ):
#             resultStr = resultStr + ''
#         else:
#             resultStr = resultStr + etree.tostring(e, encoding='unicode')

#     return resultStr

# XMLElem = etree.fromstring("<div>I am<name>Jhon <last.name> Corner</last.name></name>.I work as <job>software engineer</job><end meta='bio' />.</div>")
# print(innerXML(XMLElem))

# tree = etree.fromstring('<html><head><title>foo</title></head><body><div class="name"><p>foo</p></div><div class="name"><ul><li>bar</li></ul></div></body></html>')
# for elem in tree.xpath("//div[@class='name']"):
#      # pretty_print ensures that it is nicely formatted.
#      print(etree.tostring(elem, pretty_print=True))

from lxml import html
import urllib.request

def ordered_set(alist):
    # Creates an ordered set of unique items
    mmap = {}  # implements hashed lookup
    oset = []  # storage for set

    for item in alist:
    # Save unique items in input order
        if item not in mmap:
            mmap[item] = 1
            oset.append(item)
    return oset








# headers = {}
# headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"

# url='https://jobs.sanctuary-group.co.uk/search'
# # url='https://en.wikipedia.org/wiki/Web_scraping'
# req = urllib.request.Request(url, headers=headers)
# resp = urllib.request.urlopen(req)

# tree = html.fromstring(resp.read())
# expressText = '//ul[@class="pagination"]/li/a/@href'
# expressionConcat = expressText.strip().replace("\n", " | ") 

# mmap = {}
# oset = []

# data = tree.xpath(expressionConcat)

# for i in data:
#     if i not in mmap:
#         mmap[i] = 1
#         oset.append(i)
# print(oset)

def getChildXpath(xpathObj, listObj):
    x = []
    for i in listObj:
        x.append(xpathObj.xpath(i))
    all_lists = sum(x, [])
    return all_lists


headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"

url='https://jobs.sanctuary-group.co.uk/search'
# url='https://en.wikipedia.org/wiki/Web_scraping'
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)

tree = html.fromstring(resp.read())
expressText = '//ul[@class="pagination"]/li'
expressionConcat = expressText.strip().replace("\n", " | ") 

expressTextTwo = './a/@href\n./a/@href'

data = tree.xpath(expressionConcat)
testSplit = expressTextTwo.strip().splitlines()

testListTest = []

for i in data:
    y = getChildXpath(i, testSplit)
    testListTest.append(y)

unique_data = list(ordered_set(tuple(x) for x in testListTest))
print(unique_data)
# print(testSplit)


# for i in range(len(data)):


# expressText = '//*[@id="mw-content-text"]/div/ul[1]/li/a/text()\n//*[@id="mw-content-text"]/div/ul[1]/li/text()[1]'
# data = tree.xpath('//*[@id="mw-content-text"]/div/ul[1]/li/a/text() | //*[@id="mw-content-text"]/div/ul[1]/li/text()[1]')
# print(len(data))
# uniqueData = set()
# for i in range(len(data)):




























# from single_page import SinglePage

# Convert string to json
# queryString = "{'type': ' Single', 'url': 'http://oshinit.com/', 'subUrl': '', 'file': '', 'connectTo': '', 'row_search': '//h5/text()', 'column_search': ''}".replace("\'", "\"")
# stringToDict = json.loads(queryString)

# Create instance
# testrun = SinglePage('test2', stringToDict)
# testrun.test_run()

# print(testrun.get_result())
# Check for intsances of object
# testScrapper = SinglePage('A')
# testScrapper.test()

# testScrapper2 = SinglePage('B')
# testScrapper2.test()

# testScrapper3 = SinglePage('C')
# testScrapper3.test()

# testScrapper4 = SinglePage('d')
# testScrapper4.base_test()

# checkIntances = SinglePage('D')
# checkIntances.printIntances()
