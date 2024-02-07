from django.urls import path
from .views import index_view, TemplViewForm
urlpatterns = [
    path('', TemplViewForm.as_view(), name='landing'),
    # path('fv/', FV.as_view(), name='landing'),
    path('', index_view, name='index'),
    # добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing
]
