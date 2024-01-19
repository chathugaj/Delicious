from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Menu page"""
    template_name = "home/index.html"
