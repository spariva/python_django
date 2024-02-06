from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Juego
# quiere herencia tipo layout en templates y paginación

class IndexView(generic.ListView):
    template_name = "juegos/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Juego.objects.order_by("-number_players")[:5]


class DetailView(generic.DetailView):
    model = Juego
    template_name = "juegos/detail.html"
