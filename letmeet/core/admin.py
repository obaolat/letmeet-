from django.contrib import admin
from .models import Profile
from .models import Post, LikePost, FollowersCount

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)

# Register your models here.
 