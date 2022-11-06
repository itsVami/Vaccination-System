from django import template
from ..models import Category 

register = template.Library()

@register.simple_tag
def Web_Title ():
    return "سامانه واکسیناسیون کرونا"

@register.inclusion_tag('vaccine/partials/category_navbar.html')
def Category_Navbar ():
    return {
        "category" : Category.objects.filter(status=True)
    }

@register.inclusion_tag('registration/partials/link.html')
def link(request , link_name , content , classes):
    return {
        "request" : request ,
        "link_name" : link_name ,
        "link" : "adminpanel:{}".format(link_name) ,
        "content" : content ,
        "classes" : classes ,
    }