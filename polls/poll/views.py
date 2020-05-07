from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView
from django.views.generic.base import View

from poll.models import Question, Choice


class PollList(ListView):
    template_name = 'list.html'
    model = Question


class DoPoll(View):
    def get(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs['question'])
        choices = Choice.objects.filter(question=question)
        print(choices)

        return render(request, 'do.html', {'choice_list': choices, 'question': question})

    def post(self, request, *args, **kwargs):
        print(request.POST.get)
        question = Question.objects.get(id=kwargs['question'])
        result = request.POST.get('choice')
        choice = Choice.objects.get(id=result)
        choice.votes += 1
        choice.save()

        return redirect('/result/' + str(question.id))


class PollResult(View):
    def get(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs['question'])
        choices = Choice.objects.filter(question=question)
        print(choices)

        return render(request, 'result.html', {'choice_list': choices, 'question': question})
