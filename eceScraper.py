import urllib
import httplib
import re


url  = "http://ece.uprm.edu/~eaponte/4103/"

page = urllib.urlopen(url).read()

positions= [m.start() for m in re.finditer("href=", page)]

for i in positions:
        ending= page.find("\">", i)
        fileurl = url + page[i+6:ending-1]
        try:
                h = httplib.HTTPConnection(fileurl)
                h.connect()
                h.request('GET', fileurl)
                r =  h.getresponse()
                if r.status == 200:
                        urllib.urlretrieve(fileurl, page[i+6:ending-1])
                else:
                        continue
        except:
                continue