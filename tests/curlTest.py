import pycurl


# Generic https tor test

c1 = pycurl.Curl()
c1.setopt(pycurl.URL, 'https://check.torproject.org/?lang=en-US&small=1')
c1.setopt(pycurl.PROXY, 'localhost')
c1.setopt(pycurl.PROXYPORT, 9050)
c1.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)

c1.perform() 

# Google https tor post request
c1 = pycurl.Curl()
c1.setopt(pycurl.URL, 'https://encrypted.google.com/search?hl=en&source=hp&biw=&bih=&q=sdgf&btnG=Google+Search')
c1.setopt(pycurl.PROXY, 'localhost')
c1.setopt(pycurl.PROXYPORT, 9050)
c1.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)

c1.perform() 

