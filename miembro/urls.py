from django.urls import path
from miembro.views import miembro
from miembro.views import agregarMiembro
from django.conf import settings
from django.conf.urls.static import static
from miembro.views import eliminarMiembro
from miembro.views import detalleMiembro



urlpatterns = [
    path('miembro/',miembro,name='miembro'),
    path('agregarMiembro/',agregarMiembro,name='agregarMiembro'),
    path('miembro/eliminarmiembro/<int:codigo>/', eliminarMiembro, name='eliminarMiembro'),
    path('detalleMiembro/',detalleMiembro, name='detalleMiembro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
