# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#the-register-decorator
from django.contrib import admin
from .models import PostArticle, CustomizeBlog, Rating, Reply, Notify
from django.contrib.auth import get_user_model

User = get_user_model()


# class AuthorAdmin(admin.ModelAdmin):
# exclude the fields mentioned with exclude = ('code_bar_lateral_up', 'code_bar_lateral_down',)
# exclude = ('code_bar_lateral_up', 'code_bar_lateral_down',)
# Include the fields what we want with fields = ('code_bar_lateral_up', 'code_bar_lateral_down',)
# exclude = ('code_bar_lateral_up', 'code_bar_lateral_down','code_bar_lateral_footer',)


# admin.site.register(Code, AuthorAdmin)

class PostArticleAdmin(admin.ModelAdmin):
    exclude = ('number_of_ping_backs', 'color_font_footer',)
    prepopulated_fields = {'slug': ('title',)}

    # Returning articles related with a user
    def get_queryset(self, request):
        if request.user.is_superuser:
            return PostArticle.objects.all()
        else:
            return PostArticle.objects.filter(user_id=request.user)

    # Returning user name related with authenticated user
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
                This is a method to work with foreign field in the site administration
                """
        if request.user.is_superuser and (db_field.name == 'user_id'):
            kwargs['queryset'] = User.objects.filter(is_staff=True)
        else:
            kwargs['queryset'] = User.objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AuthorAdmin(admin.ModelAdmin):
    exclude = ('color_font_footer',)


class CustomizeBlogAdmin(admin.ModelAdmin):
    fieldsets = (
        ('This section tries about the section head', {
            'fields': ('name',
                       'title_of_blog',
                       'description_of_blog',
                       'ico_image_therty_by_therty_px',
                       'menu_image',
                       'logo_image',
                       'notification_image',
                       'profile_default_image',
                       'background_color_head_footer',
                       'background_gradient_color_head',
                       'color_font_head'),
            'classes': ('collapse',),
            # 'description': "This is the head setting"
        }),
        ('If active setting is selected then this [setting] will be applied to the blog', {
            'fields': ('active_setting',),
            # 'description': "This is the head setting"
        }),
    )


admin.site.register(PostArticle, PostArticleAdmin)
admin.site.register(CustomizeBlog, CustomizeBlogAdmin)
admin.site.register(Rating)
admin.site.register(Reply)
admin.site.register(Notify)
