from django.conf.urls import url
from django.contrib import admin

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'solar_conflict.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#)

#from django.conf.urls import url
#from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]