from django.shortcuts import render

def home(request):
    var_de_mierda = "Vete con tu puta madre cabrón!!!."
    context = {
        "var_de_mierda": var_de_mierda
    }

    return render(request, "lyra/home.html", context)
