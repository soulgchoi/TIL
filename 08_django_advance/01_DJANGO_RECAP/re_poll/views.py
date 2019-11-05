from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice
# from .forms import ChoiceModelForm


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 're_poll/question_detail.html', {
        'question': question,
    })


# def upvote(request, question_id, ??):
#     return redirect(??)



# def new_choice(request):
#     form
#     if form.is_valid():
#         choice = form.save(commit=False)
#         if choice.content == '':
#             choice.question_id = ??
#             choice.save()
#             choice.vote += 1