from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/admin/login/?next=/")
def index(request):
    return render(request, "index.html", {})

@login_required(login_url="/admin/login/?next=/")
def inventory(request):
    return render(request, "inventory/index.html", {})
