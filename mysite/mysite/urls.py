from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
]
