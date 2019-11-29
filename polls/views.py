from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

import ldclient
import random

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        ldclient.set_sdk_key("sdk-8e89675e-2e6a-4297-94a6-aa582b659146") 
        choice = random.choice([True, False]) 
        if choice is True:
            user = {
              "key": "UNIQUE IDENTIFIER",
              "firstName": "Bob",
              "lastName": "Loblaw",
              "custom": {
                "groups": "beta_testers"
              }
            }
        else:
            user = {
              "key": "BRUCE IDENTIFIER",
              "firstName": "Bruce",
              "lastName": "Da'Man",
              "custom": {
              "groups": "teach"
              }
            }

        show_feature = ldclient.get().variation("poll-1", user, False)
        if not show_feature:
            return None
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    # Note that if two concurrent users attempted to vote at the same time,
    # you now have a race condition and the values may not get appropriately incremented
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
