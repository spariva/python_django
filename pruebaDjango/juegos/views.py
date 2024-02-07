from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Juego
# quiere herencia tipo layout en templates y paginación

class IndexView(generic.ListView):
    template_name = "juegos/index.html"


class DetailView(generic.DetailView):
    model = Juego
    template_name = "juegos/detail.html"
