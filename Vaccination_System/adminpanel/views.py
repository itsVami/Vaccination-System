from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin 
from patient.models import Patient
from vaccine.models import Vaccine
from .mixins import  AuthorsAccessMixin , VaccineDeleteAccessMixin , AuthorAccessMixin , VaccineFiledsMixin , PatientDeleteAccessMixin 
from django.urls import reverse_lazy
from .models import Admin
from .forms import ProfileForm , PatientForm
from django.db.models import Q
from django.shortcuts import render , get_object_or_404

# My Views

class PatientList(LoginRequiredMixin , ListView):
    queryset = Patient.objects.all()
    template_name = "registration/home.html"



class PatientCreate(AuthorsAccessMixin , CreateView):
    model = Patient
    template_name = "registration/patient_create_update.html"
    form_class = PatientForm
    success_url = reverse_lazy('adminpanel:home')



class PatientUpdate(AuthorAccessMixin , UpdateView):
    model = Patient
    template_name = "registration/patient_create_update.html"
    form_class = PatientForm
    success_url = reverse_lazy('adminpanel:home')



class PatientDelete(PatientDeleteAccessMixin , DeleteView):
    model = Patient
    template_name = "registration/patient_confirm_delete.html"
    success_url = reverse_lazy('adminpanel:home')

    

class VaccineCreate(AuthorsAccessMixin , VaccineFiledsMixin , CreateView):
    model = Vaccine
    template_name = "registration/vaccine_create_update.html"




class VaccineUpdate(AuthorAccessMixin , VaccineFiledsMixin , UpdateView):
    model = Vaccine
    template_name = "registration/vaccine_create_update.html"



class VaccineDelete(VaccineDeleteAccessMixin , DeleteView):
    model = Vaccine
    template_name = "registration/vaccine_confirm_delete.html"
    success_url = reverse_lazy('adminpanel:vaccine_list')



class VaccineList(LoginRequiredMixin , ListView):
    template_name = "registration/vaccine_list.html"
    queryset = Vaccine.objects.available()



class Profile(LoginRequiredMixin , UpdateView):
    template_name = "registration/profile.html"
    model = Admin
    form_class = ProfileForm
    success_url = reverse_lazy('adminpanel:profile')

    def get_object(self):
        return Admin.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile , self).get_form_kwargs()
        kwargs.update({
            'user' : self.request.user 
        })
        return kwargs



class SearchList(ListView):
    template_name = "registration/search_list.html"

    def get_queryset(self):
        search = self.request.GET.get('q')
        return Patient.objects.filter(Q(national_code__icontains = search) | Q(name__icontains = search) | Q(phone_number__icontains = search)) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context



def StatusControl(request):
    patient_count = Patient.objects.all().count()
    vaccine_count = Vaccine.objects.all().count()


    if request.user.is_authenticated and request.user.special_user :
        context = {
            "patient_count" : patient_count ,
            "vaccine_count" : vaccine_count ,
            
        }
        return render(request , "registration/status_control.html" , context)
    else :
        return render(request , "registration/eror404.html")



class PatientCard(AuthorAccessMixin , DetailView):
    template_name = "registration/patient_card.html"

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Patient , pk = pk)