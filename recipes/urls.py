from django.urls import path
<<<<<<< HEAD
from recipes.views import home, adicionar_item, remover_item, obter_lista
from django.conf import settings
from django.conf.urls.static import static
=======
from django.http import HttpResponse
from recipes.views import home, my_View




>>>>>>> 2c49d046b3788a96df4482ca904ae9eb2a3169c5

urlpatterns =[

<<<<<<< HEAD
    path("", home, name="home"),
    path('adicionar-item/', adicionar_item, name='adicionar_item'),
    path('remover-item/<int:item_id>/', remover_item, name='remover_item'),
    path("obter-lista/", obter_lista, name="obter_lista"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
path("my_View/", my_View),
    path("", home),
]
>>>>>>> 2c49d046b3788a96df4482ca904ae9eb2a3169c5
