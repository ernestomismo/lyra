from django.shortcuts import render
import torch

def gen_data_view(request):
    return render(request, "lyra/show_data.html", {})

def show_data(request):
    #tensor = generate_data(0, 0)
    return render(request, "lyra/data.html", {})

def generate_data(start, end):
    # Create data
    start = 0
    end = 1
    step = 0.02
    X = torch.arange(start, end, step).unsqueeze(dim=1)

    return X