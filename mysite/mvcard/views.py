from django.contrib import messages
# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post, Category,Contact,Testimonials,Portfolio



def index(request):
    return render(request,'mvcard/index.html')

def  about(request):
    testimonials=Testimonials.objects.all()
    return render(request, 'mvcard/about.html',{'testimonials':testimonials})

def  resume(request):
    return render(request, 'mvcard/resume.html')

def  portfolio(request):
    portfolios = Portfolio.objects.all()
    cat= Category.objects.all()
    return render(request, 'mvcard/portfolio.html',{'portfolios':portfolios,'cat':cat})

def  blog(request):
    post = Post.objects.order_by('-post_date')   
    return render(request, 'mvcard/blog.html',{'post':post})

#def  contact(request):
#   return render(request, 'mvcard/contact.html')


def contact(request):
    if request.method == 'POST':
        contact=Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.phone=phone
        contact.message=message 
        contact.save()
        return HttpResponse("<h1>Thanks you!! We will reach you soon</h1>")
       # messages.success(request,'Message sent!! Will get back soon')
        #return redirect('contact') # replace 'success_page' with the name of the page you want to redirect to after the contact is saved
   # else:
    return render(request, 'mvcard/contact.html') # replace 'contact.html' with the name of your contact form template

