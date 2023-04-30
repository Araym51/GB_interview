from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import ProductInformationForm
from .models import ProductInformation

# Create your views here.


def products_veiw(request):
    return render(request, 'main_app/index.html', {'products': ProductInformation.objects.all()})


def create_product(request):
    data = dict()
    if request.method == 'POST':
        form = ProductInformationForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = ProductInformation.objects.all()
            data['products_html'] = render_to_string('main_app/goods_list.html', {'products': products})
        else:
            data['form_html'] = render_to_string('main_app/good_create.html', {'form': form}, request=request)

    else:
        data['form_is_valid'] = False
        data['form_html'] = render_to_string('main_app/good_create.html', {'form': ProductInformationForm()}, request=request)

    return JsonResponse(data)
