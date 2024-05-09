from django.shortcuts import render, redirect

# Create your views here.
from .forms import FormDataForm
def index(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after form submission
    else:
        form = FormDataForm()
    return render(request, 'form_app/form.html', {'form': form})

