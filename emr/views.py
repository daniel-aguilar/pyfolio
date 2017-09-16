from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from .forms import MedicalRecordForm
from .models import MedicalRecord, Patient

# Create your views here.


# TODO: Move patient templates to a 'patients' directory

class PatientList(LoginRequiredMixin, ListView):
    model = Patient


class PatientDetail(LoginRequiredMixin, DetailView):
    model = Patient


class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    success_url = reverse_lazy('emr:patient-list')
    fields = '__all__'
    template_name_suffix = '_create_form'


class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    success_url = reverse_lazy('emr:patient-list')
    fields = '__all__'
    template_name_suffix = '_update_form'


class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('emr:patient-list')


class MedicalRecordCreate(LoginRequiredMixin, View):
    template_name = 'emr/medical_records/create_form.html'
    form_class = MedicalRecordForm
    model = MedicalRecord

    def get(self, request, patient_pk):
        patient = get_object_or_404(Patient, pk=patient_pk)
        return render(request, self.template_name, {'form': self.form_class(), 'patient': patient})

    def post(self, request, patient_pk):
        patient = get_object_or_404(Patient, pk=patient_pk)
        form = self.form_class(request.POST)

        if form.is_valid():
            medical_record = form.save(commit=False)
            medical_record.patient = patient
            medical_record.save()

            return redirect('emr:patient-detail', patient.id)

        else:
            return render(request, self.template_name, {'form': form, 'patient': patient})


class MedicalRecordUpdate(LoginRequiredMixin, UpdateView):
    model = MedicalRecord
    fields = [
        'current_condition',
        'current_treatment',
        'reference',
        'physical_exploration',
        'diagnosis',
        'treatment_to_follow',
        'additional_notes',
    ]
    template_name = 'emr/medical_records/update_form.html'

    def get_success_url(self):
        medical_record = self.get_object()
        patient_id = medical_record.patient.id
        return reverse('emr:patient-detail', args=[patient_id])
