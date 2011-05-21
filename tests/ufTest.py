import urllib2_file
import urllib2

data = { 'foo':         'bar',
         'file1':    {'fd' : open("/root/testpilot.png"),
                      'filename':    'testpilot.png'}
        }


proxy_support = urllib2.ProxyHandler({"http" : "http://localhost:8118"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

u = urllib2.urlopen('http://test.lovelyspam.org/receive/', data)

print u.read()
