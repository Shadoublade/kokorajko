from django.contrib import admin

from .models import Question
from .models import Post
from .models import Comment

admin.site.register(Question)
admin.site.register(Post)
admin.site.register(Comment)
