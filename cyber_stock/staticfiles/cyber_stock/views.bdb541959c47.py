from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class BaseView(LoginRequiredMixin, TemplateView):
  pass