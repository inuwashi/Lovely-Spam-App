import pycurl

## {{{ http://code.activestate.com/recipes/576422/ (r1)
# --------- upload_file.py ----------------
# upload binary file with pycurl by http post
c = pycurl.Curl()
c.setopt(c.POST, 1)
c.setopt(pycurl.PROXY, 'localhost')
c.setopt(pycurl.PROXYPORT, 9050)
c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
c.setopt(c.HTTPPOST, [("fileupload1", (c.FORM_FILE, "/root/testpilot.png"))])
c.setopt(c.URL, "http://75aiiotc26qp4j2y.onion/Boys/~upload")
#c.setopt(c.VERBOSE, 1)
c.perform()
c.close()
print "that's it ;)"


