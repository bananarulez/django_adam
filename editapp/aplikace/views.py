from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .models import Cvut

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

#def upload(request):
#    if request.method == 'POST':
#        uploaded_file = request.FILES['document']
#        fs = FileSystemStorage()
#        fs.save(uploaded_file.name, uploaded_file)
#    return render(request, 'upload.html')

class DeleteData(DeleteView):
    model = Cvut
    template_name = 'data_delete.html'
    success_url = reverse_lazy('data')

