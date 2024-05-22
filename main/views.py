from django.shortcuts import render, redirect
from .forms import ContactForm

def main(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return  redirect('home')
    else:
        form = ContactForm()
    return render(request, 'main/index.html', {'form': form})
