from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
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


class PatientCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Patient
    success_url = reverse_lazy('emr:patient-list')
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_message = _('Patient %(patient_full_name)s added')

    def get_success_message(self, cleaned_data):
        patient = self.object
        return self.success_message % dict(patient_full_name=patient.full_name())


class PatientUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Patient
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_message = _('Personal information updated')

    def get_success_url(self):
        patient = self.get_object()
        return reverse('emr:patient-detail', args=[patient.id])


class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('emr:patient-list')
    success_message = _('Patient %(patient_full_name)s removed')

    # HACK: DeleteView currently does not support SuccessMessageMixin, so this method had to be overridden
    def delete(self, request, *args, **kwargs):
        patient = self.get_object()
        messages.success(request, self.success_message % dict(patient_full_name=patient.full_name()))
        return super().delete(self, request, *args, **kwargs)


class MedicalRecordCreate(LoginRequiredMixin, View):
    template_name = 'emr/medical_records/create_form.html'
    form_class = MedicalRecordForm
    model = MedicalRecord
    success_message = _('Medical record created')

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

            messages.success(request, self.success_message)
            return redirect('emr:patient-detail', patient.id)

        else:
            return render(request, self.template_name, {'form': form, 'patient': patient})


class MedicalRecordUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
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
    success_message = _('Medical record updated')

    def get_success_url(self):
        medical_record = self.get_object()
        patient_id = medical_record.patient.id
        return reverse('emr:patient-detail', args=[patient_id])
