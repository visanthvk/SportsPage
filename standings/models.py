from django.db import models

class Standings(models.Model):
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
    TEAM = (
        ('coral','Coral'),
        ('emerald', 'Emerald'),
        ('diamond', 'Diamond'),
        ('ruby','Ruby'),
        ('pearl', 'Pearl'),
        ('sapphire', 'Sapphire'),
    )
    team1 = models.CharField(max_length=10,choices=TEAM)
    team2 = models.CharField(max_length=10,choices=TEAM)
    team3 = models.CharField(max_length=10,choices=TEAM)
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    team3_score = models.IntegerField()
    def __str__(self):
        temp = self.gender+"-"+self.sport
        return temp

    class Meta:
        unique_together = (('gender', 'sport'),)
        verbose_name_plural = "Standings"