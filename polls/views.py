from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
# #### from django.template import loader      # everything marked with '#### ' uses loader, but this is replaced by render()

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # #### template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    # #### HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question.id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twicw if a 
        # user hits the Back button.
        return HttpResponse(reverse('polls:results', args=(question_id,)))
