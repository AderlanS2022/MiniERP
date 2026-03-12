from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # AUTH
    path("accounts/", include("django.contrib.auth.urls")),

    # DASHBOARD (HOME)
    path("", include("core.urls")),

    # MÓDULOS
    path("produtos/", include("produtos.urls")),
    path("estoque/", include("estoque.urls")),
    path("pdv/", include("pdv.urls")),
    path("financeiro/", include("financeiro.urls")),
    path("compras/", include("compras.urls")),
    path("relatorios/", include("relatorios.urls")),
    path("usuarios/", include("usuarios.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)