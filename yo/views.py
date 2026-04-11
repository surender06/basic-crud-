from calendar import c
from tkinter import W

from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .models import Yoga
from .forms import YogaForm
from django.urls import reverse_lazy
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin

class SignUpCreateView(CreateView):
      form_class=UserCreationForm
      template_name="registration/SignUp.html"
      success_url=reverse_lazy('login')

      

class YogaCreateView(LoginRequiredMixin,CreateView):
    model=Yoga
    template_name="yo/yoga_form.html"
    success_url=reverse_lazy('list')
    form_class=YogaForm

class YogaListView(LoginRequiredMixin,ListView,SuccessMessageMixin):
     model=Yoga
     fields="__all__"
     template_name="yo/yoga_list.html"
     success_url=reverse_lazy('list')
     success_message="your form is submitted successfully ❤️"
     paginate_by = 5

     def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
           return Yoga.objects.filter(name__icontains=query)

        return Yoga.objects.all()


class YogaUpdateView(LoginRequiredMixin,UpdateView):
      model=Yoga
      fields="__all__"
      template_name="yo/yoga_form.html"
      success_url=reverse_lazy('list')
      
class YogaDeleteView(LoginRequiredMixin,DeleteView):
      model=Yoga
      template_name="yo/yoga_list.html"
      success_url=reverse_lazy('list')

