import re
import mechanize
import mimetypes
import random
import sys
import Image, ImageDraw
import string, tempfile

def genRandomText(wordCount=4):
    words = open('/home/dj/app/actionScripts/nouns.txt').readlines()
    cleanWords = [w.strip() for w in words]
    return ' '.join(random.sample(cleanWords,wordCount))


def prepPayload(uri):
    """
    Some image boards recodnize images so we chnage them a little
    """
    # Randomize file name
    payloadNameParts = uri.split(".")
    payloadName = "%s%s.%s" % (''.join(payloadNameParts[:-1]),genRandomText(1),payloadNameParts[-1])
    
    # Move to /tmp 
    payloadNameParts = payloadName.split("/")
    payloadName = "/tmp/%s" % payloadNameParts[-1]

    # Add some random pixels
    img  = Image.open(uri)
    draw = ImageDraw.Draw(img)
    width,height = img.size
    draw.point((random.randint(1,width),random.randint(1,height)), fill=random.randint(1,128))
    del draw
    img.save(payloadName)
    del img
    return open(payloadName)
    
    


def doIBPost(url, payload, name=None, email=None, subject=None, message=None, success=None):
    """
    Post image to a chan style image board

    Input
    url : Url of image board page with upload form.
    payload : File object of the image to be posted. Must be JPG, GIF or PNG.
    name : Name of the poster.
    email : Email address (links from Name).
    subject : Title for the post.
    message : Contet of text decription, we be randome if not provided.
    success : An optional text value the form sould return a success.
              If provided it will be compared to the results of the form.

    Output :
    If success is provided then True in the provided text exits with in 
    results or False if it isn't. 

    If no success value is provided the just return the HTML result of the form.
    """

    
    payload = prepPayload(payload)

    # Get and approve mime type
    mimeType = mimetypes.guess_type(payload.name)[0]
    allowedTypes = ['image/png','image/gif','image/jpeg']
    if mimeType not in allowedTypes:
        raise TypeError('Only PNG, GIF and JPG allowed.')




    # Make sure we have all the neaded values
    if not name: name = genRandomText(2)
    if not subject: subject = genRandomText()
    if not email:
        email = '%s@%s.%s' % tuple(genRandomText(2).split()+[random.choice(['com','net','org']),])
    if not message: 
        message = genRandomText(random.randint(20, 45))+(random.randint(45, 65)*'\n')+genRandomText(random.randint(35, 55))+(random.randint(45, 65)*'\n')+genRandomText(random.randint(20, 45))



    br = mechanize.Browser()
    br.set_proxies({"http" : "http://localhost:8118"})


    br.open(url)

    b1 = br.response()
    br.select_form(nr=0)
    br.form['name']=name
    br.form['email']=email
    br.form['subject']=subject
    br.form['message']=message
    br.form.add_file(payload, mimeType, payload.name.split("/")[-1])

    assert br.viewing_html()
    #print '\ntitle\n',br.title()
    #print '\nurl\n',b1.geturl()
    #print '\ninfo\n',b1.info()
    #print '\nhtml\n',b1.read()
    #print '\nform\n',br.form


    b2 = br.submit(nr=0)

    assert br.viewing_html()
    result  = b2.read()
    #print '\ntitle\n',br.title()
    #print '\nurl\n',b2.geturl()
    #print '\ninfo\n',b2.info()
    #print '\nhtml\n',result
    

    
    if not success:
        return result
    else:
        if success in result:
            return True
        else:
            return False

     
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Post an image to a chan style image borad.')
    parser.add_argument('-u','--url',
                        help='Url of image board page with upload form',
                        required=True
                        )
    parser.add_argument('-p','--payload',
                        help='File to post',
                        #type=file,
                        required=True
                        ) 
    parser.add_argument('-n','--name',
                        help='Name of the poster',
                        )
    parser.add_argument('-e','--email',
                        help='Email address (links from Name)'
                        )
    parser.add_argument('-s','--subject',
                        help='Title for post',
                        )
    parser.add_argument('-m','--message',
                        help='Contet of text decription, we be randome if not provided'
                        )

    args = parser.parse_args()
    
    #try:
    res = doIBPost(
        url=args.url,
        payload=args.payload,
        name=args.name,
        email=args.email,
        subject=args.subject,
        message=args.message)
    #except Exception, e:
    #    sys.exit("An issue occured:\n%s" % str(e))

    print res
