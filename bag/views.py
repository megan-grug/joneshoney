from django.shortcuts import render

# Create your views here.


def view_bag(request):
    ''' A view that presents the shopping cart contents page '''

    return render(request, 'bag/bag.html')
