from django.shortcuts import render

# Create your views here.
def datos(request):
    return render(request,'templatesDatosApp2/datos.html')

def dato1(request):
    data={
        "imagen":"imagenes/controlador.jpg",
        "dato":"Controlador",
    }
    return render(request,'templatesDatosApp2/datos.html',data)
def dato2(request):
    data={
        "imagen":"imagenes/cdj.jpg",
        "dato":"Reproductor CDj",
    }
    return render(request,'templatesDatosApp2/datos.html',data)
def dato3(request):
    data={
        "imagen":"imagenes/vinilo.jpg",
        "dato":"Reproductor de Vinilo",
    }
    return render(request,'templatesDatosApp2/datos.html',data)