from django.contrib import admin
from blog.models import Post
#blog의 model에  Post를 참조한다.
# Register your models here.

admin.site.register(Post)