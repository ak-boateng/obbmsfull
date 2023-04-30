from django.contrib import admin
from .models import Donor, User

# Register your models here.
admin.site.register(Donor)
admin.site.register(User)
#admin.site.register(Donor_Partner)