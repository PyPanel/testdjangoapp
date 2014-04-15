from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'testdjangoapp.views.home', name='home')
)
