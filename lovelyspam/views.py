from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers



from settings import MEDIA_URL,MEDIA_ROOT
from lovelyspam.models import *


def postForm(request):
    """
    This view will allow ser to select which traget 
    he wants to spam and with what.
    """

    return render_to_response(
        'postFrom.html',
        {"sites": TargetSite.objects.all(),
         "payloads" : Payload.objects.filter(loadType='I'),
         "blurbes" : Blurb.objects.all(),
         "MEDIA_URL": MEDIA_URL}
        )


def getTargets(request,siteID):
    """
    Return a JSON list of active targets in the requested sites
    """
    site = TargetSite.objects.get(id=int(siteID))
    siteTargets = site.target_set.filter(active=True)
    #Sanitizing URL from JSON string. Dont want to publish this crap.
    for st in siteTargets: st.url="Try again loser"
    data = serializers.serialize("json", siteTargets)
    return HttpResponse(data,content_type='application/json')

def getDescription(request,siteID):
    """
    Return a JSON list of active targets in the requested sites
    """
    site = TargetSite.objects.get(id=siteID)
    return HttpResponse(site.description)


def getBlurb(request,blurbID,wordCount):
    """
    Retunr the conetnt of the blurb identified by the ID.
    Will return up to work count. IF wourd count is 0 
    return the entire blurb.
    """

    theBlurb  = Blurb.objects.get(id=blurbID)
    if int(wordCount) == 0:
        crap = theBlurb.crap
    else:
        from django.utils.text import truncate_html_words
        crap = truncate_html_words(theBlurb.crap, wordCount)

    return HttpResponse(crap)


def doPost(request,targetID):
    """
    Call in the reqiered script and post some spam.
    """
    
    theTarget = Target.objects.get(id=targetID)

    scriptAttributes = theTarget.script.scriptattribute_set.all()
    
    # Get all the script command line attributes
    attributes = ""


    for attr in scriptAttributes:
        #attributes+=attr.name+str(request.GET)

        # Deal with URL as the one attributes that is provided by the target
        if attr.name == "URL":
            attributes += ' %s %s' % (attr.flag, theTarget.url) 
            continue

        try:
            attributes += ' %s %s' % (attr.flag, request.GET[attr.name])
        except KeyError:
            try:
                refID  = int(request.GET[attr.name+"_ID"])
            except KeyError:
                if attr.required:
                    return HttpResponse("Missing attribute : %s" % attr.name)
            else:
                #Obj refrance as opposed to the actual value
                if attr.name == "PAYLOAD":
                    value = Payload.objects.get(id =refID).load
                    attributes += ' %s %s%s' % (attr.flag, MEDIA_ROOT, value)
                elif attr.name == "MESSAGE":
                    value = Blurb.objects.get(id =refID).crap
                    attributes += ' %s "%s"' % (attr.flag, value)
                else:
                    return HttpResponse("Unknow attribute : %s" % attr.name)

    cmd ="python %s %s" % (theTarget.script.script, attributes)

    import commands
    out = commands.getoutput(cmd)
    if "refresh" in out.decode('utf-8'):
        return HttpResponse("You just spammed some pedo's days")
    else:        
        return HttpResponse("Something went wrong, please try again.")

    #return HttpResponse(cmd+'<br>'+'_-_'.join(out.decode('utf-8').split(' ')) )

