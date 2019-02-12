from django.db import models

class Results(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=10,choices=GENDER)
    SPORT = (
        ('badmiton','Badmiton'),
        ('ballbadmiton','Ball Badmiton'),
        ('basketball', 'Basketball'),
        ('cricket','Cricket'),
        ('chess', 'Chess'),
        ('football', 'Football'),
        ('handball','Handball'),
        ('hockey','Hockey'),
        ('kabaddi', 'Kabaddi'),
        ('khokho', 'Kho-Kho'),
        ('tabletennis','Table Tennis')
    )
    sport = models.CharField(max_length=20,choices=SPORT)
    date = models.DateField(auto_now=False, auto_now_add=False)
    match_number = models.IntegerField()
    TEAM = (
        ('direct','Direct'),
        ('coral','Coral'),
        ('emerald', 'Emerald'),
        ('diamond', 'Diamond'),
        ('ruby','Ruby'),
        ('pearl', 'Pearl'),
        ('sapphire', 'Sapphire'),
    )
    team1 = models.CharField(max_length=10,choices=TEAM)
    team2 = models.CharField(max_length=10,choices=TEAM)
    team1_score = models.CharField(max_length=10)
    team2_score = models.CharField(max_length=10)
    winner = models.CharField(max_length=10,choices=TEAM,default=team1)
    def __str__(self):
        temp = self.gender+"-"+self.sport+"-mno:"+str(self.match_number)
        return temp
    
    class Meta:
        verbose_name_plural = "Results"