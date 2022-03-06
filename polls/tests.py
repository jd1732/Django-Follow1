from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime

class QuestionModelTest(TestCase):
    
    
    def test_recently_pub_for_future(self):
        
        t=timezone.now()+datetime.timedelta(days=30)
        future_q=Question(pub_date=t)
        self.assertIs(future_q.recently_Pub(), False)
        
        
    def test_recently_pub_for_old(self):
        
        t=timezone.now()-datetime.timedelta(days=1, seconds=1)
        old_q=Question(pub_date=t)
        self.assertIs(old_q.recently_Pub(),False)
    
    def test_recently_pub_for_recent(self):
        
        t=timezone.now()-datetime.timedelta(hours=23,minutes=59, seconds=59)
        recent_q=Question(pub_date=t)
        self.assertIs(recent_q.recently_Pub(),True)
