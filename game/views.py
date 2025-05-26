from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.conf import settings
from .models import PlayerScore
import random
import os
BASE_DIR = settings.BASE_DIR

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@login_required
def game_view(request):
    choices = ['rock', 'paper', 'scissors']
    user_choice = request.GET.get('choice')
    computer_choice = random.choice(choices)
    result = ''

    if user_choice:
        if user_choice == computer_choice:
            result = 'Нічия!'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            result = 'Ви перемогли!'
            score, _ = PlayerScore.objects.get_or_create(user=request.user)
            score.score += 1
            score.save()
        else:
            result = 'Ви програли!'

    scores = PlayerScore.objects.select_related('user').order_by('-score')[:10]
    return render(request, 'game/index.html', {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result,
        'scores': scores,
    })
