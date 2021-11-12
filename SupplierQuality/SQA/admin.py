from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PPAP, Claim, Part, Subassembly, Supplier_T1, User

admin.site.register(User, UserAdmin)
admin.site.register(Supplier_T1)
admin.site.register(Subassembly)
admin.site.register(Part)
admin.site.register(PPAP)
admin.site.register(Claim)

# Register your models here.
