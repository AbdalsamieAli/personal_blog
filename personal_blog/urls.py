from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from blog import views as blog_views
from profile_app import views as profile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", profile_views.index, name="home"),
    path("blog/", blog_views.BlogListView.as_view(), name="bloglist"),
    path("<int:blog_id>", blog_views.detail, name="detail"),
    path("contact/", profile_views.contact, name="contact"),
    path("projects/", blog_views.ProjectListView.as_view(), name="projects")
    ]

if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()
