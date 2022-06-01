from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = "helpout/home.html"
