from django.urls import path
from recipes.views import home, adicionar_item, remover_item, obter_lista
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", home, name="home"),
    path('adicionar-item/', adicionar_item, name='adicionar_item'),
    path('remover-item/<int:item_id>/', remover_item, name='remover_item'),
    path("obter-lista/", obter_lista, name="obter_lista"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
