from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ItemListaCompra

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'list': ItemListaCompra.objects.all(),
    })

@csrf_exempt
def adicionar_item(request):
    if request.method == 'POST':
        data = request.POST
        item = data.get('item')
        quantidade = data.get('quantidade', 1)

        novo_item = ItemListaCompra.objects.create(item=item, quantidade=quantidade)
        lista = list(ItemListaCompra.objects.values())

        return JsonResponse({'lista': lista})
    elif request.method == 'GET':
        # Lógica para lidar com solicitações GET, se necessário
        return HttpResponse("Solicitação GET recebida.")
    else:
        return HttpResponse("Método não suportado.", status=405)

@csrf_exempt
def remover_item(request, item_id):
    if request.method == 'POST':
        try:
            item = ItemListaCompra.objects.get(id=item_id)
            item.delete()
            lista = list(ItemListaCompra.objects.values())
            return JsonResponse({'lista': lista})
        except ItemListaCompra.DoesNotExist:
            return JsonResponse({'error': 'Item não encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Erro interno ao remover o item'}, status=500)
    elif request.method == 'GET':
        # Lógica para lidar com solicitações GET, se necessário
        return HttpResponse("Solicitação GET recebida.")
    else:
        return HttpResponse("Método não suportado.", status=405)

# Nova view para obter a lista de compras
def obter_lista(request):
    lista = list(ItemListaCompra.objects.values())
    return JsonResponse({'lista': lista})
