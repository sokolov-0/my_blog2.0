from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.blog.feeds import LatestPostFeed


handler403 = 'apps.blog.views.tr_handler403' # New
handler404 = 'apps.blog.views.tr_handler404' # New
handler500 = 'apps.blog.views.tr_handler500' # New

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feeds/latest/', LatestPostFeed(), name = 'latest_post_feed'),
    path('', include('apps.blog.urls')),
    path('', include('apps.accounts.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]