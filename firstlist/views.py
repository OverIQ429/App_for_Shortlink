from multiprocessing.context import DefaultContext

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import DefaultLink
from .forms import DefaultLinkForm, DefaultLinkFormGet
import random
import string

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def create_link(request):
    if request.method == 'POST':
        original_link = request.POST.get('original_link')
        print(original_link)
        if original_link:
            print("original_link is", original_link)
            short_code = generate_short_code()
            generated_link = f"http://127.0.0.1:8000/first/shortlink/{short_code}"
            DefaultLink.objects.create(
                original_link=original_link,
                shortlink=short_code
            )
            request.session['generated_link'] = generated_link
            return redirect('show_link')

    return render(request, 'firstlist/linkgenerat.html')

def show_link(request):
    generated_link = request.session.get('generated_link', '')
    return render(request, 'firstlist/showlink.html', {'generated_link': generated_link})

def redirect_short_link(request, short_code):
    link = get_object_or_404(DefaultLink, shortlink=short_code)
    return redirect(link.original_link)