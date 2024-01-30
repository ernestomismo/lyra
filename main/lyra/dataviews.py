from django.shortcuts import render
import torch

def gen_data_view(request):
    return render(request, "lyra/show_data.html", {})

def show_data(request):
    start = int(request.POST["start"])
    end = int(request.POST["end"])
    tensor = generate_data(end)
    context = {"data": tensor,}
    return render(request, "lyra/show_data.html", context)

def generate_data(end):
    # Create data

    X = torch.arange(end)
    
    return X.tolist