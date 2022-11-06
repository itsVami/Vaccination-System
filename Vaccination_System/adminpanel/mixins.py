from django.http import Http404
from django.shortcuts import redirect , get_object_or_404
from patient.models import Patient
from .models import Admin





class VaccineFiledsMixin():
    
    def dispatch(self, request, *args, **kwargs):
        self.fields = ["name" , "slug" , "country" , "count" , "description" , "picture" , "availablity" , "category"]
        
        return super().dispatch(request, *args, **kwargs)



class VaccineDeleteAccessMixin():
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.special_user :
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You Can Not See This Page.")



class AuthorsAccessMixin():
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.special_user or request.user.is_author :
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('adminpanel:home')
        else:
            return redirect('login')



class PatientDeleteAccessMixin():
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.special_user :
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You Can Not See This Page.")



class AuthorAccessMixin():
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.special_user or request.user.is_author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You Can Not See This Page.")
