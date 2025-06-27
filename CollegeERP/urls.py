from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


class LogoutGetView(LogoutView):
    # permitimos explícitamente ambos métodos
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        # aquí llamamos al post() original para hacer el logout
        return super().post(request, *args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('info/', include('info.urls')),
    path('api/', include('apis.urls')),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='info/login.html'), name='login'),
    path('accounts/logout/',
               LogoutGetView.as_view(template_name='info/logout.html'), name='logout'),
]
