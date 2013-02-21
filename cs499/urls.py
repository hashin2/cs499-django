from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^api/', include('cs499.cs499_app.views.api.urls'))
)
