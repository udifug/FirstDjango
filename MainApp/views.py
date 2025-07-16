from MainApp.models import Item
from django.shortcuts import render, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


# Create your views here.
def home_page(request):
    return render(request, "index.html")


def about(request):
    text = '<h1>Автор сайта: Олег</h1>'
    return HttpResponse(text)


def item_list(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items.html", context)


def item_page(request, id):
    try:
        item = Item.objects.get(id = id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Not Found 404. Предмет с id={id} Не найдет')
    context = {
        'item':item
    }
    return render(request, "item.html", context)
