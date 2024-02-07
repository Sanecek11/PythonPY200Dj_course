from django.shortcuts import render, redirect
from .forms import TemplateForm
from django.views import View
from django.http import HttpRequest, JsonResponse
from django.views.generic import FormView


# class TemplView(View):
#     def get(self, request):
#         return render(request, 'landing/index.html')
#
#     def post(self, request):
#         received_data = request.POST
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         user_agent = request.META.get('HTTP_USER_AGENT')
#
#         form = TemplateForm(received_data)
#         if form.is_valid():
#             name = form.cleaned_data.get("name")
#             email = form.cleaned_data.get("email")
#             message = form.cleaned_data.get("message")
#
#             response_data = {
#                 'name': name,
#                 'email': email,
#                 'message': message,
#                 'ip_address': ip,
#                 'user_agent': user_agent
#             }
#             return JsonResponse(response_data, json_dumps_params={"indent": 4})


class TemplViewForm(FormView):
    template_name = 'landing/index.html'
    form_class = TemplateForm

    def form_valid(self, form):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        user_agent = self.request.META.get('HTTP_USER_AGENT')

        data = form.cleaned_data
        data["ip"] = ip
        data["user_agent"] = user_agent

        return JsonResponse(data, json_dumps_params={"indent": 4})



def index_view(request):
    if request.method == "GET":
        return render(request, 'landing/index.html')
