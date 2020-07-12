from django.db import models
# from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Inquiry(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("Название вакансии", max_length=150)
    company = models.CharField("Название  компании",blank=True, max_length=150)
    employment = models.CharField("Тип занятости", max_length=100)
    worktime = models.CharField("График работы", max_length=100)
    exp = models.CharField("Опыт работы", max_length=100)
    skills =  models.CharField("Ключевые навыки",blank=True, max_length=1000)
    text = models.CharField("Подробное описание",blank=True, max_length=5000)
    result = models.IntegerField("Результат вычисления",blank=True)


    
               
               



