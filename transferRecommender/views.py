from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def transferRecommender(request):
    return render(request, "transferRecommender/transferRecommender.html", {})