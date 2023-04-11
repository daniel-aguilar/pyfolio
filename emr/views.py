import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, UpdateView, View
from pkg_resources import resource_stream

from pyfolio.settings.production import LANGUAGE_CODE

from .forms import MedicalRecordForm
from .models import MedicalRecord, Patient

# Create your views here.


class PatientList(LoginRequiredMixin, TemplateView):
    template_name = 'emr/patients/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['js_data'] = {
            'urls': {
                'datatablesLanguage': reverse('emr:api-datatables-language'),
                'patientList': reverse('emr:api-patient-list'),
                'viewPatient': reverse('emr:patient-detail'),
                'updatePatient': reverse('emr:patient-update'),
                'deletePatient': reverse('emr:patient-delete'),
            },
            'lang': {
                'view': pgettext('verb', 'View'),
                'edit': _('Edit'),
                'delete': _('Remove'),
            },
        }
        return context


class PatientListApi(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        patient_fields = ['id', 'identification', 'first_name', 'last_name']
        patient_list = Patient.objects.values(*patient_fields)

        return JsonResponse({'data': list(patient_list)})


class PatientDetail(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'emr/patients/detail.html'


class PatientCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Patient
    template_name = 'emr/patients/create_form.html'
    success_url = reverse_lazy('emr:patient-list')
    fields = '__all__'
    success_message = _('Patient %(patient_full_name)s added')

    def get_success_message(self, cleaned_data):
        patient = self.object
        return self.success_message % dict(patient_full_name=patient.full_name())


class PatientUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Patient
    template_name = 'emr/patients/update_form.html'
    fields = '__all__'
    success_message = _('Personal information updated')

    def get_success_url(self):
        patient = self.get_object()
        return reverse('emr:patient-detail', args=[patient.id])


class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'emr/patients/confirm_delete.html'
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


class DataTablesLanguageFile(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        # HACK: Small patch to localize DataTables
        if get_language() == LANGUAGE_CODE.split('-')[0]:
            with resource_stream('emr.resources.datatables', 'spanish.json') as language_file:
                return JsonResponse(json.load(language_file))
        else:
            return JsonResponse(None, safe=False)
