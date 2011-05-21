import pycurl

## {{{ http://code.activestate.com/recipes/576422/ (r1)
# --------- upload_file.py ----------------
# upload binary file with pycurl by http post
c = pycurl.Curl()
c.setopt(c.POST, 1)
c.setopt(c.URL, "http://test.lovelyspam.org/receive/")
c.setopt(c.HTTPPOST, [("file1", (c.FORM_FILE, "/root/testpilot.png"))])
c.setopt(pycurl.PROXY, 'localhost')
c.setopt(pycurl.PROXYPORT, 9050)
c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
#c.setopt(c.VERBOSE, 1)
c.perform()
c.close()
print "that's it ;)"


