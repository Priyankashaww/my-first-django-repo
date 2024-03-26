from django.contrib import admin
# Register your models here.

from story.models import customer
admin.site.register(customer)


from story.models import admins
admin.site.register(admins)

from story.models import reserve
admin.site.register(reserve)


from story.models import contactt
admin.site.register(contactt)