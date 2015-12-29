from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # newsletter urls:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),

    url(r'^about/$', 'src.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # blog urls:
    url(r'^blog/$', 'blog.views.post_list', name='blog'),
    url(r'^blog/post/(?P<pk>[0-9]+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^blog/post/new/$', 'blog.views.post_new', name='post_new'),
    url(r'^blog/post/(?P<pk>[0-9]+)/edit/$', 'blog.views.post_edit', name='post_edit'),
    url(r'^blog/drafts/$', 'blog.views.post_draft_list', name='post_draft_list'),
    url(r'^blog/post/(?P<pk>[0-9]+)/publish/$', 'blog.views.post_publish', name='post_publish'),
    url(r'^blog/post/(?P<pk>[0-9]+)/remove/$', 'blog.views.post_remove', name='post_remove'),
    url(r'^blog/post/(?P<pk>[0-9]+)/comment/$', 'blog.views.add_comment_to_post', name='add_comment_to_post'),
    url(r'^blog/comment/(?P<pk>[0-9]+)/approve/$', 'blog.views.comment_approve', name='comment_approve'),
    url(r'^blog/comment/(?P<pk>[0-9]+)/remove/$', 'blog.views.comment_remove', name='comment_remove'),
]
if settings.DEBUG:
    # allow static files to be served in dev environment
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
