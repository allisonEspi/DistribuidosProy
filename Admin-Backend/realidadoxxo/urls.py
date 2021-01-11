from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from productos import views
from productos.views import *
#from productos.views import CategoriaViewSet,ComentarioViewSet,EscaneosViewSet,FavoritoViewSet,GaleriaViewSet,LocalViewSet,NotificacionesViewSet,PermisoViewSet,RolViewSet,RolpermisoViewSet,TelefonoViewSet,UsuarioViewSet,tablaLocal
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'comentario', ComentarioViewSet)
router.register(r'escaneo', EscaneosViewSet)
router.register(r'favorito', FavoritoViewSet)
router.register(r'galeria', GaleriaViewSet)
router.register(r'local', LocalViewSet)
router.register(r'permiso', PermisoViewSet)
router.register(r'notificaciones', NotificacionesViewSet)
router.register(r'rol', RolViewSet)
router.register(r'rolpermiso', RolpermisoViewSet)
router.register(r'telefono', TelefonoViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'publicidad', PublicidadViewSet)




# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('adminD/', include(router.urls)),
    path('', views.login, name="login"),
    path('index/', views.index, name="index"),
    path('tablaUsuario/', views.tablaUsuario, name="tablaUsuario"),
    path('tablaLocal/', views.tablaLocal, name="tablaLocal"),
    path('tablaLocal/(?P<id_local>)$', localDelete, name="localDelete"),
    path('tablaCategoria/', views.tableCategoria, name="tablaCategoria"),
    path('tablaCategoria/(?P<id_categoria>)$', categoriaDelete, name="categoriaDelete"),
    path('tablaFavorito/', views.tableFavorito, name="tablaFavorito"),
    path('tablaFavorito/(?P<id_favorito>)$', favoritoDelete, name="favoritoDelete"),
    path('tablaTelefono/', views.tableTelefono, name="tablaTelefono"),
    path('tablaGaleria/', views.tableGaleria, name="tablaGaleria"),
    path('tablaGaleria2/', views.tableGaleria2, name="tablaGaleria2"),
    path('registrarCategoria/', registrarCategoria, name="registrarCategoria"),
    path('registrarLocal/', registrarLocal, name="registrarLocal"),
    path('registrarUsuario/', registrarUsuario, name="registrarUsuario"),
    path('registrarPublicidad/', registrarPublicidad, name="registrarPublicidad"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('logout/', views.logout_view, name='logout'),
    path('localDelete/', views.localDelete, name='localDelete'),
    path('usuarioDelete/', views.usuarioDelete, name='usuarioDelete'),
    path('editarLocal/', views.editarLocal, name='editarLocal'),
    path('editarUsuario/', views.editarUsuario, name='editarUsuario')
    
]

urlpatterns += [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)