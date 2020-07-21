from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from shop.models import inventory, categories


def index(request):
    itemObj = inventory.objects.all()
    category_List = []
    itemList = ()
    categoryObj = categories.CATEGORY
    for cKey, cName in categoryObj:
        for name in cName[:1]:
            category_List.append(cName)
    if not itemObj:
        raise ValidationError("No item available.")
    else:
        itemList = itemObj
    return render(request, "index.html", {"item_list": itemList, "categoryList": category_List})
