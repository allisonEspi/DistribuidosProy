from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Permiso(models.Model):
    # Field name made lowercase.
    id_permiso = models.AutoField(db_column='id_Permiso', primary_key=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = "Permisos"


class Rol(models.Model):
    # Field name made lowercase.
    id_rol = models.AutoField(db_column='id_Rol', primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.tipo


class Rolpermiso(models.Model):
    # Field name made lowercase.
    id_rolpermiso = models.AutoField(
        db_column='id_RolPermiso', primary_key=True)
    # Field name made lowercase.
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE,
                               blank=True, null=True, related_name='user_rol_rolpermiso')
    # Field name made lowercase.
    id_permiso = models.ForeignKey(
        Permiso, on_delete=models.CASCADE, blank=True, null=True, related_name='user_rol_permiso')
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Rolpermiso'
        verbose_name_plural = "Rolpermisos"

    def __str__(self):
        return str(self.id_rol)


class Categoria(models.Model):
    # Field name made lowercase.
    id_categoria = models.AutoField(db_column='id_Categoria', primary_key=True)
    tipo = models.CharField(max_length=12, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.tipo


class User(AbstractUser):
    email = models.CharField(primary_key=True, max_length=40)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    contrasena = models.CharField(max_length=12, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    # Field name made lowercase.
    src_imagen = models.ImageField(
        verbose_name="Imagen", db_column='src_Imagen', max_length=200, blank=True, null=True)
    id_rol = models.ForeignKey(
        Rol, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email


class Local(models.Model):
    id_local = models.AutoField(db_column='id_Local', primary_key=True)
    # models.IntegerField(db_column='id_Local', primary_key=True)  # Field name made lowercase.
    # Field name made lowercase.
    nombre_comercial = models.CharField(
        db_column='nombre_Comercial', max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    # Field name made lowercase.
    src_logo = models.ImageField(
        verbose_name="Imagen", db_column='src_Logo', max_length=100, blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    slogan = models.CharField(max_length=50, blank=True, null=True)
    estrellas = models.IntegerField(blank=True, null=True)
    vistas = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=25, blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, blank=True, null=True)
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)
    adminLocal = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = "Locales"

    def __str__(self):
        return self.nombre_comercial


class Favorito(models.Model):
    # Field name made lowercase.
    id_favorito = models.AutoField(db_column='id_Favorito', primary_key=True)
    id_local = models.ForeignKey(
        Local, on_delete=models.CASCADE, blank=True, null=True)
    # Field name made lowercase.
    id_usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = "Favoritos"

    def __str__(self):
        return self.id_favorito


class Notificaciones(models.Model):
    # Field name made lowercase.
    id_notificacion = models.AutoField(
        db_column='id_Notificacion', primary_key=True)
    alcance = models.CharField(max_length=20, blank=True, null=True)
    notificacion = models.CharField(max_length=50, blank=True, null=True)
    # Field name made lowercase.
    id_usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Notificaciones'
        verbose_name_plural = "Notificacioness"

    def __str__(self):
        return self.notificacion


class Escaneos(models.Model):
    # Field name made lowercase.
    id_escaneos = models.AutoField(db_column='id_Escaneos', primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    lugar = models.CharField(max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=10, blank=True, null=True)
    # Field name made lowercase.
    id_usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Escaneos'
        verbose_name_plural = "Escaneoss"

    def __str__(self):
        return self.id_escaneos


class Comentario(models.Model):
    # Field name made lowercase.
    id_comentario = models.AutoField(
        db_column='id_Comentario', primary_key=True)
    id_local = models.ForeignKey(
        Local, on_delete=models.CASCADE, blank=True, null=True)
    # Field name made lowercase.
    id_usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    comentario = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.id_comentario


class Galeria(models.Model):
    # Field name made lowercase.
    id_contenido = models.AutoField(db_column='id_Contenido', primary_key=True)
    # Field name made lowercase.
    id_local = models.ForeignKey(
        Local, on_delete=models.CASCADE, blank=True, null=True)
    # Field name made lowercase.
    src_path = models.ImageField(
        verbose_name="Imagen", db_column='src_Path', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = "Galerias"

    


class Telefono(models.Model):
    # Field name made lowercase.
    id_telefono = models.AutoField(db_column='id_Telefono', primary_key=True)
    # Field name made lowercase.
    id_local = models.ForeignKey(
        Local, on_delete=models.CASCADE, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = "Telefonos"

    def __str__(self):
        return self.id_telefono


class Publicidad(models.Model):
    id_publicidad = models.AutoField(
        db_column='id_publicidad', primary_key=True)
    id_usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    Fecha_Creacion = models.DateTimeField(auto_now=True)
    src_imagen = models.ImageField(
        verbose_name="Imagen", db_column='src_imagen', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Publicidad'
        verbose_name_plural = "Publicidades"

    def __str__(self):
        return self.id_publicidad
