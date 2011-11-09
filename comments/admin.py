'''@package noiro.helpdesk.admin
Helpdesk admin site registration
'''

from django.contrib import admin
from comments.models import Comment

admin.site.register(Comment, admin.ModelAdmin)
