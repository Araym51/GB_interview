from django.urls import path

"""
6. Настроить файл urls.py внутреннего каталога проекта. Он должен содержать два шаблона url-адресов:
привязку к url-адресу админки проекта (будет в файле по умолчанию после создания проекта) и привязку
к набору шаблонов url-адресов созданного приложения (оператор include).
"""

app_name = 'main_app'

urlpatterns = [
    # path('', views.IndexTemplateView.as_view(), name='index'),
]