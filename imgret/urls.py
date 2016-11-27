from django.conf.urls import include, url
from django.contrib import admin

from images.views import ImageView


urlpatterns = [
    url(r'^$', ImageView.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
]
