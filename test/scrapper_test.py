import sys

# print(sys.path)

sys.path.append('D:/python-project/Web-scrapper---python/scrapper/')

from single_page import SinglePage


# Check for intsances of object
testScrapper = SinglePage('A')
testScrapper.test()

testScrapper2 = SinglePage('B')
testScrapper2.test()

testScrapper3 = SinglePage('C')
testScrapper3.test()

testScrapper4 = SinglePage('d')
testScrapper4.base_test()

checkIntances = SinglePage('D')
checkIntances.printIntances()
