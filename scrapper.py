import urllib.request

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
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = resp.read()

            saveFile = open(textFile, "wb")
            saveFile.write(respData)
            # saveFile.write(str(respData))
            saveFile.close()
        except Exception as e:
            print(str(e))
