from django.db import models
import datetime
from django.utils import timezone
class Question(models.Model):
    ques_text=models.CharField(max_length=(150))
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.ques_text
    def recently_Pub(self):
        return timezone.now()-datetime.timedelta(days=1) <=self.pub_date <= timezone.now()
    
class Choices(models.Model):
    question=models.ForeignKey(Question, models.CASCADE)
    choice_text=models.CharField(max_length=(150))
    vote=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
    
