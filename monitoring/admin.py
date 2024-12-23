from django.contrib import admin

from .models import User   , \
                    Workout, \
                    Content


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'weight', 'date')


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('date', 'nickname', 'minutes', 'distance', 'calories', 'user')


class ContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'platform', 'is_movie', 'user')


admin.site.register(User, UserAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Content, ContentAdmin)
