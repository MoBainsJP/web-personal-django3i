from django.shortcuts import render, HttpResponse

# Create your views here.

html_base= """
      "<h1>Mi pagina virtual</h1>
      <u1>
          <li><a href="/">Portada</a></li>
            <li><a href="/about/">Acerca de.....</a></li>
            <li><a href="/portafolio/">Portafolio</a></li>
            <li><a href="/contact/">contacto del grupo....</a></li>
       <u1>  
"""
def home(request):
    return render(request,"core/home.html")
def about(request):
    return render(request,"core/about.html")

def contact(request):
   return render(request,"core/contact.html")
