from django.contrib import admin
from app.lovelyspam.models import *

class ScriptAttributeInline(admin.TabularInline):
    model=ScriptAttribute
    pass

class ActionScriptAdmin(admin.ModelAdmin):
    inlines = [
        ScriptAttributeInline,
        ]
    pass


class TargetSiteAdmin(admin.ModelAdmin):
    pass

class TargetAdmin(admin.ModelAdmin):
    pass

class PayloadAdmin(admin.ModelAdmin):
    pass

class BlurbAdmin(admin.ModelAdmin):
    pass

class ActionAdmin(admin.ModelAdmin):
    pass





#admin.site.register(ScriptAttribute, ScriptAttributeInline)
admin.site.register(ActionScript, ActionScriptAdmin)
admin.site.register(TargetSite, TargetSiteAdmin)
admin.site.register(Target, TargetAdmin)
admin.site.register(Payload, PayloadAdmin)
admin.site.register(Blurb, BlurbAdmin)
admin.site.register(Action, ActionAdmin)
