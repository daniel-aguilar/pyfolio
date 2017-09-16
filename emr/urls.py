from django.conf.urls import url

from .views import (MedicalRecordCreate, MedicalRecordUpdate, PatientCreate,
                    PatientDelete, PatientDetail, PatientList, PatientUpdate)

app_name = 'emr'
urlpatterns = [
    # Patients
    url(r'^patients/$', PatientList.as_view(), name="patient-list"),
    url(r'^patients/(?P<pk>\d+)/$', PatientDetail.as_view(), name="patient-detail"),
    url(r'^patients/create/$', PatientCreate.as_view(), name="patient-create"),
    url(r'^patients/update/(?P<pk>\d+)/$', PatientUpdate.as_view(), name="patient-update"),
    url(r'^patients/delete/(?P<pk>\d+)/$', PatientDelete.as_view(), name="patient-delete"),

    # Medical Records
    url(r'^medical-records/create/(?P<patient_pk>\d+)/$', MedicalRecordCreate.as_view(), name='medical-record-create'),
    url(r'^medical-records/update/(?P<pk>\d+)/$', MedicalRecordUpdate.as_view(), name='medical-record-update'),
]
