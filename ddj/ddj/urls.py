"""
Definition of urls for ddj.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^question/$', app.views.question_list, name='question_list'),
    url(r'^question/(?P<pk>[0-9]+)/$',app.views.detail, name='detail'),
    url(r'^question/(?P<pk>[0-9]+)/results/$',app.views.results, name='results'),
    url(r'^question/(?P<pk>[0-9]+)/vote/$',app.views.vote, name='vote'),
    url(r'^post_list$', app.views.post_list, name='post_list'),
    url(r'post/(?P<pk>[0-9]+)/$', app.views.post_detail, name='post_detail'),
    url(r'post/new/$', app.views.post_new, name='post_new'),
    url(r'post/(?P<pk>[0-9]+)/edit/$', app.views.post_edit, name='post_edit'),
    url(r'drafts/$', app.views.post_draft_list, name='post_draft_list'),
    url(r'post/(?P<pk>[0-9]+)/publish/$', app.views.post_publish, name='post_publish'),
    url(r'post/(?P<pk>[0-9]+)/remove/$', app.views.post_remove, name='post_remove'),
    url(r'post/(?P<pk>[0-9]+)/comment/$', app.views.add_comment_to_post, name='add_comment_to_post'),
    url(r'comment/(?P<pk>[0-9]+)/approve/$', app.views.comment_approve, name='comment_approve'),
    url(r'comment/(?P<pk>[0-9]+)/remove/$', app.views.comment_remove, name='comment_remove'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
