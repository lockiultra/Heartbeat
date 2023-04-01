from menu.models import MenuItem

def menu_context(request):
    menu = MenuItem.objects.all()
    return {'object_list': menu}