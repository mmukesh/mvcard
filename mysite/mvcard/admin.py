from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Post,Contact,Testimonials,Portfolio


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Testimonials)
admin.site.register(Portfolio)

