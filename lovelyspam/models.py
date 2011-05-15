from django.db import models

class ActionScript(models.Model):
    name = models.CharField(max_length=255)
    script = models.FilePathField(path='/home/dj/app/actionScripts/', match='.*py$')
    
    def __unicode__(self):
        return self.name

class ScriptAttribute(models.Model):
    TYPE_CHOICES = (
        ('S', 'String'),
        ('F', 'File'),
        ('I', 'Integer'),
        ('D', 'DB Refrance'),
        ) 
    name = models.CharField(max_length=255)
    attributeType = models.CharField(max_length=1, choices=TYPE_CHOICES)
    flag = models.CharField(max_length=10)
    script = models.ForeignKey(ActionScript)
    required = models.BooleanField()

    def __unicode__(self):
        return self.name


class TargetSite(models.Model):
    """
    Sites containing chiled porngraphy.
    """
    name = models.CharField(max_length=255)
    description  = models.TextField(null=True, blank=True)
    baseUrl = models.URLField(verify_exists=False)

    def __unicode__(self):
        return self.name


class Target(models.Model):
    """
    Specific target to spam, Image borad etc.
    """
    name = models.CharField(max_length=255)
    url = models.URLField(verify_exists=False)
    captcha = models.BooleanField()
    description  = models.TextField(null=True, blank=True)
    site = models.ForeignKey(TargetSite)
    script = models.ForeignKey(ActionScript)
    active  = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name



class Payload(models.Model):
    TYPE_CHOICES = (
        ('I', 'Image'),
        ('V', 'Video'),
        )
    load = models.FileField(upload_to='payloads')
    loadType = models.CharField(max_length=1, choices=TYPE_CHOICES)
    name = models.CharField(max_length=255,null=True, blank=True)

    def __unicode__(self):
        return self.load.name


class Blurb(models.Model):
    name = models.CharField(max_length=255)
    crap  = models.TextField()

    def __unicode__(self):
        return self.name

class Action(models.Model):
    when = models.DateTimeField(auto_now=True)
    whichTarget = models.ForeignKey(Target)
    whichPayload = models.ForeignKey(Payload)
    whichBlurb = models.ForeignKey(Blurb)

    def __unicode__(self):
        return '%s on %s ' % (whichTarget,str(self.when))

