from MainApp.models import Item
from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.contrib import messages


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
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Not Found 404. Предмет с id={id} Не найдет')
    context = {
        'item': item
    }
    return render(request, "item.html", context)


def item_add(request):
    if request.method == "GET":
        return render(request, "add_product_form.html")
    elif request.method == "POST":
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        count = request.POST.get('count')
        description = request.POST.get('description')
        try:
            count = int(count)
        except (ValueError, TypeError):
            return HttpResponse("Неверное значение поля count", status=400)

        Item.objects.create(name=name, brand=brand, count=count, description=description)
        messages.success(request,'Товар успешно добавлен!')

        return redirect('items-list')
