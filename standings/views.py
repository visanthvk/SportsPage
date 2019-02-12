from django.shortcuts import render
from .models import Standings
# Create your views here.
def index(request):
    male = [0]*12
    female = [0]*9
    mteam = {'coral':0,'diamond':0,'emerald':0,'pearl':0,'ruby':0,'sapphire':0}
    fteam = {'coral':0,'diamond':0,'emerald':0,'ruby':0}
    msport = ['cricket','hockey','badmiton','tabletennis','khokho','ballbadmiton','kabaddi','chess','volleyball','basketball','football','other']
    fsport = ['basketball','chess','badmiton','tabletennis','khokho','throwball','ballbadmiton','volleyball','other']
    for i in range(len(msport)):
        temp = Standings.objects.raw('SELECT * from standings_standings where gender=%s and sport=%s',['M',msport[i]])
        if len(list(temp)) != 0:
            male[i] = 1
            mteam[temp[0].team1] += temp[0].team1_score
            mteam[temp[0].team2] += temp[0].team2_score
            mteam[temp[0].team3] += temp[0].team3_score
    for i in range(len(fsport)):
        temp = Standings.objects.raw('SELECT * from standings_standings where gender=%s and sport=%s',['F',fsport[i]])
        if len(list(temp)) != 0:
            female[i] = 1
            fteam[temp[0].team1] += temp[0].team1_score
            fteam[temp[0].team2] += temp[0].team2_score
            fteam[temp[0].team3] += temp[0].team3_score
    mranking =  sorted(mteam.items(), key=lambda kv: kv[1], reverse=True)
    franking =  sorted(fteam.items(), key=lambda kv: kv[1],reverse=True)
    standings = Standings.objects.all()
    context = {
        'standings': standings,
        'male':male,
        'female':female,
        'mteam':mteam,
        'fteam':fteam,
        'mranking':mranking,
        'franking':franking
    }
    return render(request,'standings/index.html',context)