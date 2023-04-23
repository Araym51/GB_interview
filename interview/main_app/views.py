from django.shortcuts import render

# Create your views here.


def products_veiw(request):
    return render(request, 'main_app/product_list.html')


def create_product(request):
    return render(request, 'main_app/create_product.html')
