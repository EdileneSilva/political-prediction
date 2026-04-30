from django.views.generic import TemplateView

# Create your views here.
class AccueilView(TemplateView):
    template_name = 'home.html'
