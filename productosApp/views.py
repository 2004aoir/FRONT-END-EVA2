from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'templatesProductosApp/index.html')

def electronica(request):
    data={
        "titulo":"Electronica",
        "producto1":"MAC",
        "producto2":"Celular",
        "producto3":"PlayStation",
        "imagen":"imagenes/producto.png",
        "url":"https://ww2.movistar.cl/",
    }
    return render(request,'templatesProductosApp/productos.html',data)

def juguetes(request):
    data={
        "titulo":"Juguetes",
        "producto1":"Auto de juguete",
        "producto2":"Avion de juguete",
        "producto3":"Muñeca",
        "imagen":"imagenes/producto.png",
        "url":"https://portales.inacap.cl/",

    }
    return render(request,'templatesProductosApp/productos.html',data)

def ropa(request):
    data={
        "titulo":"Ropa",
        "producto1":"Pantalon",
        "producto2":"Polera",
        "producto3":"Blusa",
        "imagen":"imagenes/producto.png",
        "url":"https://www.youtube.com/?app",
    }
    return render(request,'templatesProductosApp/productos.html',data)