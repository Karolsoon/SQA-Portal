from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PPAP, Part, Subassembly, Supplier_T1, User

admin.site.register(User, UserAdmin)
admin.site.register(Supplier_T1)
admin.site.register(Subassembly)
admin.site.register(Part)
admin.site.register(PPAP)

# Register your models here.
