from django.shortcuts import render
from discussions.models import Reward
# Create your views here.

def leaderHome(request):
    users = Reward.objects.all()
    context = {'users' : users}
    return render(request, 'leaderboard_home.html', context)