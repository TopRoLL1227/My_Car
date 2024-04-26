from django.views.generic import TemplateView, CreateView
from django.shortcuts import redirect, reverse


class MainView(TemplateView):
    template_name = "my_car/main.html"


def redirect_to_main(request):
    return redirect('main')
