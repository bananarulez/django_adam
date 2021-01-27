from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render


from .models import Cvut, CvutImages

class HomeView(ListView):
    model = Cvut
    template_name = 'home.html'

class ShowData(ListView):
    model = Cvut
    template_name = 'show_data.html'

class EditData(ListView):
    model = Cvut
    template_name = 'data.html'

class DataDetail(DetailView):
    model = Cvut
    template_name = 'data_detail.html'

class EditDetail(UpdateView):
    model = Cvut
    template_name = 'edit_detail.html'
    fields = '__all__'

class NewData(CreateView):
    model = Cvut
    template_name = 'data_new.html'
    fields = '__all__'



class DeleteData(DeleteView):
    model = Cvut
    template_name = 'data_delete.html'
    success_url = reverse_lazy('data')

# def ShowImage(request):
#     return render(request, 'show_image.html')

def index(request):
    posts = Cvut.objects.all()
    results = []
    for post in posts:
        obj = {
            "post": post,
            "photos": CvutImages.objects.filter(post=post)
        }
        results.append(obj)
#    return render(request, 'index.html', {"to_render": results} )
