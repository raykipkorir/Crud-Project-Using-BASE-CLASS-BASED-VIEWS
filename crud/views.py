from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView,View,RedirectView
from .forms import AddForm
from .models import User
from django.urls import reverse
# class AddView(View):
#     def get(self,request):
#         form = AddForm()
#         context = {"form":form}
#         return render(request,"crud/add.html",context)
    

            
class AddandShowView(TemplateView):
    template_name = "crud/add.html"
    def get_context_data(self,*args, **kwargs):
        form = AddForm()
        data = User.objects.all()
        context = {"form":form,"data":data}
        return context
    
    def post(self,request):
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('addandshow')
        

class EditView(TemplateView):
    template_name = "crud/update.html"
    def get_context_data(self,*args, **kwargs):
        data = User.objects.get(pk = kwargs["id"])
        form = AddForm(instance = data )
        context = {"form":form,"data":data}
        return context
    
    def post(self,request, **kwargs):
        data = User.objects.get(pk = kwargs["id"])
        form = AddForm(instance = data,data = request.POST)
        form.save()
        
        return redirect('update',id =kwargs["id"])


class UserDeleteView(RedirectView):
    url = "/add/"
    def get_redirect_url(self, *args, **kwargs):
        User.objects.get(pk = kwargs["id"]).delete()
        return super().get_redirect_url(*args, **kwargs)
