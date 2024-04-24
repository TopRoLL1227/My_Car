from django.views.generic import TemplateView, CreateView


class MainView(TemplateView):
    template_name = "my_car/main.html"
