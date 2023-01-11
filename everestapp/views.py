from django.views.generic import View, TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth import authenticate, login, logout
from everestapp.models import Category, News
from .forms import*
from django.urls import reverse,reverse_lazy
from .models import *
from django.shortcuts import render, redirect

class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        try:
            self.user = request.user
            if self.user.is_superuser and self.user.is_active:
                print("Admin only passed")
            else:
                return redirect("everestapp:adminlogin")
        except Exception as e:
            print(e)
            return redirect("everestapp:adminlogin")
        return super().dispatch(request, *args, **kwargs)

class ClientHomeView(TemplateView):
    template_name="clienthome.html"

class ClientBlogView(TemplateView):  
    template_name = "clientblog.html"

class ClientAboutView(ListView):
    template_name="clientabout.html"
    model=Category
    context_object_name='categories'

class ClientNewsView(ListView):
    template_name="clientnews.html"
    model= News
    context_object_name='news'

class ClientNewsDetailView(DetailView):
    template_name="clientnewsdetail.html"
    model= News
    context_object_name='newsdetail' 

class ClientNewsCreateView(CreateView):
    template_name="clientnewscreate.html"
    form_class=ClientNewsCreateForm
    model= News
    success_url=reverse_lazy("everestapp:clienthome")
    
class ClientNewsUpdateView(UpdateView):
    template_name="clientnewscreate.html"
    form_class=ClientNewsCreateForm
    model= News
    success_url=reverse_lazy("everestapp:clienthome")

class ClientNewsDeleteView(DeleteView):
    template_name="clientnewsdelete.html"
    model= News
    context_object_name="news"
    success_url=reverse_lazy("everestapp:clienthome")

class AdminLoginView(FormView):
    template_name = "adminlogin.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy("everestapp:clientnewscreate")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                username = user.username
                login(self.request, user)
            except Exception as e:
                print(e)
                return render(self.request, self.template_name, {"form":form,"error": "Invalid Credentials.."})
        else:
            return render(self.request, self.template_name, {"form": form, "error": "Invalid Credentials.."})
        return super().form_valid(form)