from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import evaluation
from  myapp.models import building
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


# Create your views here.
