import sys
import json
# print(sys.path)

sys.path.append('D:/python-project/Web-scrapper---python/scrapper/')

from single_page import SinglePage

# Convert string to json
queryString = "{'type': ' Single', 'url': 'http://oshinit.com/', 'subUrl': '', 'file': '', 'connectTo': '', 'row_search': '//h5/text()', 'column_search': ''}".replace("\'", "\"")
stringToDict = json.loads(queryString)

# Create instance
testrun = SinglePage('test2', stringToDict)
testrun.test_run()

print(testrun.get_result())
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
