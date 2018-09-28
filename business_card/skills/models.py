from django.db import models

# Create your models here.


class SkillRank(models.Model):
    name = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    name = models.CharField(max_length=12, unique=True)
    version = models.CharField(max_length=12, blank=True)
    # 1 - * (одна ранг - много скилов)
    rank = models.ForeignKey(SkillRank, on_delete=models.PROTECT, null=True)
    # TODO: add a user

    def __str__(self):
        # return f'{self.name} {self.version} - Rank: {self.rank.name}'
        return f'{self.name} {self.version}'

"""
>>> SkillRank.objects.all()
<QuerySet [<SkillRank: Youngling>]>
Как удалить один объект 'Youngling'???
#############
>>> SkillRank.objects.all()
<QuerySet [<SkillRank: Youngling>, <SkillRank: Padawan>, <SkillRank: Knight>, <SkillRank: Master>, <SkillRank: Grand Master>]>
Создался PK начиная с цифры 2, как начать нумерацию с начала, если первый раз ошибся со значением???

"""