from django.shortcuts import render
from .models import Results
# Create your views here.
def index(request, game='null'):
    results = Results.objects.all()
    match = [0,0,0,0,0,0,0,0]
    if(game != 'null'):
        temp = game
        sport = temp[3:]
        gender = ''
        if(temp[:3] == 'men'):
            gender = "M"
        else:
            gender = "F"
        results = Results.objects.raw("SELECT * from results_results where sport=%s and gender=%s",[sport,gender])
        for i in results:
            k = i.match_number
            match[k-1] = 1
    context = {
        'game': game,
        'results': results,
        'match':match,
        'zero':0
    }
    return render(request,'results/index.html',context)