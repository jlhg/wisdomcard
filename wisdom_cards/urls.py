from django.conf.urls import patterns, url
from example_app.views import sample_view, accounts

urlpatterns = patterns('',
                       url(r'^$', sample_view.index, name='index'),
                       url(r'post/', sample_view.post, name='post'),
                       url(r'login/', accounts.signin, name='signin'),
                       url(r'logout/', accounts.signout, name='signout'),
                       )
