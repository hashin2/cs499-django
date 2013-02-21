from django.conf.urls.defaults import patterns

urlpatterns = patterns('',

    # Test
    (r'^test/?$',
        'cs499.cs499_app.views.api.test.hello_world'),
)
