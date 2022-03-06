from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.template import loader
from .models import Question, Choices
from django.urls import reverse
from django.db.models import F
def index(request):
    latest_10_ques=Question.objects.order_by('-pub_date')[:10]
    template=loader.get_template('polls/index.html')
    context={
            'latest_10_ques':latest_10_ques
        
        }
    return HttpResponse(template.render(context,request))


def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'q': q})
   
        

def result(request, question_id):
    q=get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html",{'q':q})

def vote(request, question_id):
    q=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=q.choices_set.get(pk=request.POST['choice'])
    except(KeyError,Choices.DoesNotExist):
        return render(request, 'polls/details.html',{
                                                'q':q,
                                                'error_message':'No Choice Selected!!'
                                                
                                        })
    selected_choice.vote = F('vote')+1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:result',args=(q.id,)))