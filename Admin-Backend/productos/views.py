from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.response import Response
from django.contrib.auth import login as do_login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from .serializers import *
from .models import *
from django.db.models import F
from django.contrib.auth.hashers import make_password

#from .serializers import UserSerializer, GroupSerializer,TCategoriaSerializer,TComentarioSerializer,TEscaneosSerializer,TFavoritoSerializer,TGaleriaSerializer,TLocalSerializer,TNotificacionesSerializer,TPermisoSerializer,TRolSerializer,TRolpermisoSerializer,TTelefonoSerializer,TUsuarioSerializer
#from .models import Categoria,Comentario,Escaneos,Favorito,Galeria,Local,Notificaciones,Permiso,Rol,Rolpermiso,Telefono,User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = TCategoriaSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = TComentarioSerializer


class EscaneosViewSet(viewsets.ModelViewSet):
    queryset = Escaneos.objects.all()
    serializer_class = TEscaneosSerializer


class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = TFavoritoSerializer


class GaleriaViewSet(viewsets.ModelViewSet):
    queryset = Galeria.objects.all()
    serializer_class = TGaleriaSerializer


class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = TLocalSerializer


class NotificacionesViewSet(viewsets.ModelViewSet):
    queryset = Notificaciones.objects.all()
    serializer_class = TNotificacionesSerializer


class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = TPermisoSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = TRolSerializer


class RolpermisoViewSet(viewsets.ModelViewSet):
    queryset = Rolpermiso.objects.all()
    serializer_class = TRolpermisoSerializer


class TelefonoViewSet(viewsets.ModelViewSet):
    queryset = Telefono.objects.all()
    serializer_class = TTelefonoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = TUsuarioSerializer


class PublicidadViewSet(viewsets.ModelViewSet):
    queryset = Publicidad.objects.all()
    serializer_class = TPublicidadSerializer


def index(request):
    return render(request, 'productos/index.html')


def tablaUsuario(request):
    #obtener permisos en base al rol anteriro
    lpermisos = obtenerPermisos(request.user)
    user = User.objects.all()
    contexto = {'usuarios': user ,'permisos': lpermisos }
    return render(request, 'productos/tablaUsuario.html', contexto)


def tablaLocal(request):
    #obtener permisos en base al rol anteriro
    lpermisos = obtenerPermisos(request.user)
    local = Local.objects.all()
    contexto = {'locales': local,'permisos': lpermisos  }
    return render(request, 'productos/tablaLocal.html', contexto)


def tableCategoria(request):
    #obtener permisos en base al rol anteriro    
    lpermisos = obtenerPermisos(request.user)
    categoria = Categoria.objects.all()
    contexto = {'categorias': categoria,'permisos': lpermisos  }
    return render(request, 'productos/tablaCategoria.html', contexto)


def tableFavorito(request):
    favorito = Favorito.objects.all()
    contexto = {'favoritos': favorito}
    return render(request, 'productos/tablaFavorito.html', contexto)


def tableTelefono(request):
    #obtener permisos en base al rol anteriro
    lpermisos = obtenerPermisos(request.user)    
    telefono = Telefono.objects.all()
    contexto = {'telefonos': telefono,'permisos': lpermisos }
    return render(request, 'productos/tablaTelefono.html', contexto)


def tableGaleria(request):
    lpermisos = obtenerPermisos(request.user)
    galeria = Galeria.objects.all()
    contexto = {'galerias': galeria ,'permisos': lpermisos}
    return render(request, 'productos/tablaGaleria.html', contexto)
def tableGaleria2(request):


    galeria = Galeria.objects.all()
    contexto = {'galerias': galeria}
    return render(request, 'productos/tablaGaleria2.html', contexto)
def localDelete(request):


    if request.method == "POST":
        local = Local.objects.get(id_local=request.POST.get('local'))
        local.delete()
    return render(request, 'productos/tablaLocal.html', {"locales": Local.objects.all()})


def categoriaDelete(request, id_categoria):
    categoria = Categoria.objects.get(id_categoria=id_categoria)
    categoria.delete()
    return render(request, 'productos/tablaCategoria.html', {"categorias": Categoria.objects.all()})


def favoritoDelete(request, id_favorito):
    favorito = Favorito.objects.get(id_favorito=id_favorito)
    favorito.delete()
    return render(request, 'productos/tablaFavorito.html', {"favoritos": Favorito.objects.all()})


def telefonoDelete(request, id_telefono):
    telefono = Telefono.objects.get(id_telefono=id_telefono)
    telefono.delete()
    return render(request, 'productos/tablaTelefono.html', {"telefonos": Telefono.objects.all()})


def galeriaDelete(request, id_contenido):
    galeria = Galeria.objects.get(id_contenido=id_contenido)
    galeria.delete()
    return render(request, 'productos/tablaGaleria.html', {"galerias": Galeria.objects.all()})
# ...


@csrf_exempt
def login(request):
    # Creamos el formulario de autenticación vacío
    print("hola mundo")
    #user = authenticate(username="chjoguer", password='zywcCQAmPf')
   # print(user)
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
            print("verificando")

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                print("si existe")
                # Y le redireccionamos a la portada
                # return redirect('registroNoticias/')

                #obtener permisos en base al rol anteriro
                lpermisos = obtenerPermisos(user)

                return render(request, "productos/index.html", {'permisos': lpermisos })

        else:
            print(form.is_valid())
            print("Password o usuario incorrecto")
            return render(request, "productos/login.html", {'form': form, 'mensaje': "User o cotrnaseña iconrrecta."})

    # Si llegamos al final renderizamos el formulario
    return render(request, "productos/login.html", {'form': form, 'mensaje': ""})

def obtenerPermisos(user):
    rol = User.objects.all().select_related('id_rol').filter(email=user).values('id_rol')[0]['id_rol']
    dic = Rolpermiso.objects.all().filter(id_rol=rol).values(permiso=F('id_permiso__id_permiso'))
    l = []
    for i in dic:
        if i["permiso"] not in l:
            l.append(i["permiso"])
    return l

@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def registrarCategoria(request):
    lpermisos = obtenerPermisos(request.user)
    if request.method == 'POST':
        if(request.POST.get("tipo") != None and request.POST.get("descripcion") != None):
            categoria = Categoria(tipo=request.POST.get(
                "tipo"), descripcion=request.POST.get("descripcion"))
            categoria.save()
            # return HttpResponse(status=200)
            return render(request, 'productos/crear/crearCategoria.html')
        return HttpResponse(status=404)
    if request.method == 'GET':
        return render(request, 'productos/crear/crearCategoria.html')


@login_required(login_url='/')
def registrarLocal(request):
    lpermisos = obtenerPermisos(request.user)
    if request.method == 'POST':
        if(request.POST.get("estrella") != None and request.POST.get("slogan") != None and request.POST.get("latitud") != None and request.POST.get("longitud") != None and request.POST.get("vista") != None and request.POST.get("direccion") != None and request.POST.get("nombrec") != None and request.POST.get("like") != None and request.POST.get("descripcion") != None and request.POST.get("imagen") != None):
            local = Local(latitud=request.POST.get("latitud"), estrellas=request.POST.get("estrella"), longitud=request.POST.get("longitud"), slogan=request.POST.get("slogan"), vistas=request.POST.get(
                "vista"), descripcion=request.POST.get("descripcion"), likes=request.POST.get("like"), direccion=request.POST.get("direccion"), nombre_comercial=request.POST.get("nombrec"), src_logo=request.POST.get('imagen'))
            local.save()
            # return HttpResponse(status=200)
            return render(request, 'productos/crear/crearLocal.html',{'permisos': lpermisos })
        return HttpResponse(status=404)
    if request.method == 'GET':
        return render(request, 'productos/crear/crearLocal.html', {"categorias": Categoria.objects.all()})


@login_required(login_url='/')
def editarLocal(request):
    if request.method == 'POST':
        local = Local.objects.get(id_local=request.POST['local'])
        if(request.POST['nombrec'] != None or request.POST['nombrec'] != ''):
            local.nombre_comercial = request.POST['nombrec']
        if(request.POST['descripcion'] != None or request.POST['descripcion'] != ''):
            local.descripcion = request.POST['descripcion']
        if(request.POST['like'] != None or request.POST['like'] != ''):
            local.likes = request.POST['like']
        if(request.POST['estrella'] != None or request.POST['estrella'] != ''):
            local.estrellas = request.POST['estrella']
        if(request.POST['vista'] != None or request.POST['vista'] != ''):
            local.vistas = request.POST['vista']
        if(request.POST['direccion'] != None or request.POST['direccion'] != ''):
            local.direccion = request.POST['direccion']
        if(request.POST['longitud'] != None or request.POST['longitud'] != ''):
            local.direccion = request.POST['longitud']
        if(request.POST['latitud'] != None or request.POST['latitud'] != ''):
            local.direccion = request.POST['latitud']
        if(request.POST['slogan'] != None or request.POST['slogan'] != ''):
            local.direccion = request.POST['slogan']
        if(bool(request.FILES.get('imagen', False)) == True):
            local.src_logo = request.FILES['imagen']
        local.save()
    return render(request, 'productos/tablaLocal.html', {"locales": Local.objects.all()})


@login_required(login_url='/')
def registrarUsuario(request):
    lpermisos = obtenerPermisos(request.user)
    if request.method == 'POST':
        if(request.POST.get("email") != None and request.POST.get("nombre") != None and request.POST.get("apellido") != None and request.POST.get("contrasena") != None and request.POST.get("telefono") != None and request.POST.get("imagen") != None):
            rol = Rol.objects.all().filter(id_rol=request.POST.get("rol")).first()
            usuario = User(username=request.POST.get("email").split('@')[0], email=request.POST.get("email"), nombres=request.POST.get("nombre"), first_name=request.POST.get("nombre"), contrasena=request.POST.get(
                "contrasena"), password=make_password(request.POST.get("contrasena")), telefono=request.POST.get("telefono"), apellidos=request.POST.get("apellido"), last_name=request.POST.get("apellido"), src_imagen=request.POST.get('imagen'),id_rol=rol)
            usuario.save()
            # return HttpResponse(status=200)
            return render(request, 'productos/crear/crearUsuario.html',{'permisos': lpermisos })
        return HttpResponse(status=404)
    if request.method == 'GET':
        return render(request, 'productos/crear/crearUsuario.html', {"roles": Rol.objects.all()})


@login_required(login_url='/')
def editarUsuario(request):
    if request.method == 'POST':
        usuario = User.objects.get(email=request.POST['email'])
        if(request.POST['email'] != None or request.POST['email'] != ''):
            usuario.email = request.POST['email']
        if(request.POST['nombres'] != None or request.POST['nombres'] != ''):
            usuario.nombres = request.POST['nombres']
        if(request.POST['apellidos'] != None or request.POST['apellidos'] != ''):
            usuario.apellidos = request.POST['apellidos']
        if(request.POST['contrasena'] != None or request.POST['contrasena'] != ''):
            usuario.contrasena = request.POST['contrasena']
        if(request.POST['telefono'] != None or request.POST['telefono'] != ''):
            usuario.telefono = request.POST['telefono']
        # if(request.POST['id_rol']!=None or request.POST['id_rol']!=''):
     #       usuario.id_rol=request.POST['id_rol']
        if(bool(request.FILES.get('imagen', False)) == True):
            usuario.src_imagen = request.FILES['imagen']
        usuario.save()
    return render(request, 'productos/tablaUsuario.html', {"usuarios": User.objects.all()})


@login_required(login_url='/')
def usuarioDelete(request):
    if request.method == "POST":
        usuario = User.objects.get(email=request.POST.get('email'))
        usuario.delete()
    return render(request, 'productos/tablaUsuario.html', {"usuarios": User.objects.all()})


def registrarPublicidad(request):
    if request.method == 'POST':
        if(request.POST.get("descripcion") != None):
            publicidad = Publicidad(tipo=request.POST.get("descripcion"))
            publicidad.save()
            # return HttpResponse(status=200)
            return render(request, 'productos/crear/crearPublicidad.html')
        return HttpResponse(status=404)
    if request.method == 'GET':
        return render(request, 'productos/crear/crearPublicidad.html')
