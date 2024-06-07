from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.productos import productos
from main.forms import FlanForm

# Create your views here.
def index(req):
    context = {'productos': productos}
    return render(req, 'index.html', context)
def about(req):
    return render(req, 'about.html')
def welcome(req):
    if req.method == 'GET':
        form = FlanForm()
        context = {'form': form}
        return render(req, 'welcome.html', context)
    else:
        form = FlanForm(req.POST)
        if form.is_valid():
            return redirect('/success')
        context = {'form': form}
        return render(req, 'welcome.html', context)
    #return render(req, 'welcome.html')
# def welcome(req):
#     customer_name = req.POST['customer_name']
#     customer_email = req.POST['customer_email']
#     message = req.POST['message']
#     errores = []
#     if len(customer_name) > 64:
#         errores.append('Largo mayor a lo permitido')
#     if not '@' in customer_email:
#         errores.append('Direccion no valida')
#     if len(errores) > 0:
#         context = {'errores': errores}
#         return render(req, 'welcome.html', context)
#     else:
#         return render(req, 'index.html')
    
    #print(customer_email)
    #return HttpResponse('OK')
    #return redirect('/welcome')

def success(req):
    return render(req, 'success.html')