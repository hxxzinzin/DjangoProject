from django.shortcuts import render, redirect
from .forms import PostModelForm

def home(request):
    return render(request, "index.html")

def create(request):
    if request.method == 'POST' or request.method == "FILES":
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('toL_list')
    else:
        form = PostModelForm()
    return render(request, 'form_create.html', {'form' : form})