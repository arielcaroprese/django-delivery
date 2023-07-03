from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registro_usuario/', views.user_register , name='user_register'),
    path('iniciar_sesion/', views.user_login , name='user_login'),
    path('logout/', views.Logout.as_view() , name='user_logout'),
    path('usuario/<username>', views.UserDetailView.as_view() , name='user_detail'),
    path('editar_usuario/', views.userEdit , name='user_update')
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)