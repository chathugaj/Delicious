from django.views.generic import TemplateView


class MenuView(TemplateView):
    """Home page"""
    template_name = "menu/index.html"
