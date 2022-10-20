from django.views.generic import ListView , DetailView
from .models import Vaccine , Category
from django.shortcuts import get_object_or_404

# Vaccine Views

class VaccineList(ListView):

    queryset = Vaccine.objects.available()

    
class CategoryList(ListView):

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active() , slug = slug)
        return category.vaccines.available()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context



class VaccineDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        vaccine = get_object_or_404(Vaccine.objects.available() , slug = slug)

        return vaccine
