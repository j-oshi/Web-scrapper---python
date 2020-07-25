import urllib.request
from lxml import etree
from io import StringIO


class Scrapper:
    def __init__(self, url):
        self.url = url

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

    def get_web_content(self, textFile):
        try:
            url = self.url

            # now, with the below headers, we defined ourselves as a simpleton who is
            # still using internet explorer.
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            respData = resp.read()
            data = self.parse_html(respData)

            saveFile = open(textFile, "w")

            for element in data:
                saveFile.write(element)
                saveFile.write('\n')
            saveFile.close()
        except Exception as e:
            print(str(e))

    def parse_html(self, htmlcontent):
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO(str(htmlcontent)), parser=parser)
        nodes = tree.xpath("//a")
        # Get the url from the ref
        # links = [link.get('href', '')
        list = []
        for el in nodes:
            list.append(el.get('href', ''))
        return list
         
    # Read site robot.txt
    def get_site_robot_txt(self):
        # stream = urllib.request.urlopen(self.url + "/robots.txt")
        stream = urllib.request.urlopen(
            "https://jobs.sanctuary-group.co.uk/robots.txt")
        print(stream.read().decode("utf-8"))


scanSite = Scrapper("https://jobs.sanctuary-group.co.uk/search/")
scanSite.get_web_content('test3.txt')
# scanSite.get_site_robot_txt()
