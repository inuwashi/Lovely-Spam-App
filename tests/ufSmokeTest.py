import urllib2_file
import urllib2

data = { 'MAX_FILE_SIZ': '2097152',
         'parent':'0',
         'name':'Little Wolf',
         'email':'address@domain.com',
         'subject':'My little wolf',
         'message':'THE laws of God, the laws of man,\nHe may keep that will and can;\nNot I: let God and man decree\nLaws for themselves and not for me;\nAnd if my ways are not as theirs\nLet them mind their own affairs.\nTheir deeds I judge and much condemn,\nYet when did I make laws for them?\nPlease yourselves, say I , and they\nNeed only look the other way.\nBut no, they will not; they must still\nWrest their neighbour to their will,\nAnd make me dance as they desire\nWith jail and gallows and hell-fire.\nAnd how am I to face the odds',
         'file':{'fd' : open("/root/testpilot.png"),'filename':'testpilot.png'},
         'password' : 'aq12ws',
         
         
        }


proxy_support = urllib2.ProxyHandler({"http" : "http://localhost:8118"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

u = urllib2.urlopen('http://h3pv234d2h6vov2a.onion/ch/anime/imgboard.php')
print u.read()
