from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    """Renders the front page.

    """
    return render(request, 'home.html')


def view_list(request, list_id):
    """Checks that we can view a list.

    :param request: HTTP request object as passed by urls.py.
    :param list_id: The list we want to view.

    """
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(f'/lists/{list_id}/')
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
    """Checks that we can create a new list.

    :param request: HTTP request object.
    :return: http redirects or assertion failure.
    """
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(f'/lists/{list_.id}/')

