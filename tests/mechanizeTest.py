import re
import mechanize

br = mechanize.Browser()
br.set_proxies({"http" : "http://localhost:8118"})


#data = { 'foo':         'bar',
#         'file1':    {'fd' : open("/root/testpilot.png"),
#                      'filename':    'testpilot.png'}
#        }


br.open("http://test.lovelyspam.org/form/")

b1 = br.response()
br.select_form(nr=0)
br.form['foo']="bar"
br.form.add_file(open("testpilot.png"), "image/png", "testpilot.png")

assert br.viewing_html()
print '\ntitle\n',br.title()
print '\nurl\n',b1.geturl()
print '\ninfo\n',b1.info()
print '\nhtml\n',b1.read()
print '\nform\n',br.form


b2 = br.submit(nr=0)

assert br.viewing_html()
print '\ntitle\n',br.title()
print '\nurl\n',b2.geturl()
print '\ninfo\n',b2.info()
print '\nhtml\n',b2.read()



