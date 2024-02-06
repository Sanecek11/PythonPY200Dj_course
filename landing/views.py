from django.shortcuts import render, redirect
from .forms import TemplateForm
from django.views import View
from django.http import HttpRequest, JsonResponse


# Create your views here.
class TemplView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):
        received_data = request.POST
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')

        form = TemplateForm(received_data)
        name = email = message = ''  # Default values in case form is not valid
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")

        response_data = {
            'form_data': received_data,
            'name': name,
            'email': email,
            'message': message,
            'ip_address': ip,
            'user_agent': user_agent
        }

        return JsonResponse(response_data)


 def index_view(request):
     if request.method == "GET":
         return render(request, 'landing/index.html')


# class TemplView(View):
#     def get(self, request):
#
#         if request.method == "GET":
#             return render(request, 'landing/index.html')
#
#     def post(self, request):
#         if request.method == "POST":
#             received_data = request.POST  # Приняли данные в словарь
#             x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#             if x_forwarded_for:
#                 ip = x_forwarded_for.split(',')[0]  # Getting the IP
#             else:
#                 ip = request.META.get('REMOTE_ADDR')  # Getting the IP
#             user_agent = request.META.get('HTTP_USER_AGENT')
#             form = TemplateForm(received_data)  # Передали данные в форму
#             if form.is_valid():  # Проверили, что данные все валидные
#                 name = form.cleaned_data.get("name")  # Получили очищенные данные
#                 email = form.cleaned_data.get("email")
#                 message = form.cleaned_data.get("message")
#             response_data = {
#                 'form_data': request.POST,
#                 'name': name,
#                 'email': email,
#                 'message': message,
#                 'ip_address': ip,
#                 'user_agent': user_agent
#                 }
#
#             return JsonResponse(response_data)
#         else:
#                 # return JsonResponse({'статус': 'Данные успешно отправлены!'})
#                 # return JsonResponse(form.cleaned_data)
#             return render(request, 'landing/index.html', context={"form": form})