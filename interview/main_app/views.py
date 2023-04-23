from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ProductInformationForm
from .models import ProductInformation

# Create your views here.


def products_veiw(request):
    return render(request, 'main_app/goods_list.html', {'object_list': ProductInformation.objects.all()})


def create_product(request):
    if request.method == 'POST':
        form = ProductInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductInformationForm()

    return render(request, 'main_app/good_create.html', {'form': form})
