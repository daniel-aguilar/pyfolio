from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Patient

# Create your views here.


SUCCESS_URL = reverse_lazy('emr:patient-list')

FIELDS = [
    'identification',
    'first_name',
    'last_name',
    'sex',
    'date_of_birth',
    'occupation',
    'phone_number',
    'address',
]


class PatientList(LoginRequiredMixin, ListView):
    model = Patient


class PatientDetail(LoginRequiredMixin, DetailView):
    model = Patient


class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    success_url = SUCCESS_URL
    fields = FIELDS
    template_name_suffix = '_create_form'


class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    success_url = SUCCESS_URL
    fields = FIELDS
    template_name_suffix = '_update_form'


class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = SUCCESS_URL
