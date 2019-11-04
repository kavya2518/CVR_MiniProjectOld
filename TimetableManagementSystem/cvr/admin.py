from django.contrib import admin

# register your models here.

from .models import *

admin.site.register(TimeTable)
admin.site.register(Branch)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Teacher)

admin.site.site_header="TimeTable Management System"
admin.site.site_title="TimeTable Management System"


