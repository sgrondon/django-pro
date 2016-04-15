from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

        url(r'^admin/', include(admin.site.urls)),
        url(r'', include('blog.urls')),
		url(r'^$', 'django.contrib.auth.views.login', {'template':'inicio/index.html'}, name='login'),
        url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}),
        url('^', include('django.contrib.auth.urls'))
]
