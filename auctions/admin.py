from django.contrib import admin
from .models import Listing,Comment, Bid,Visitor
# Register your models here.

admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Visitor)
