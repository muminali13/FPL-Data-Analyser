from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def teamPickRecommender(request):
    return render(request, "teamPickRecommender/teamPickRecommender.html", {})