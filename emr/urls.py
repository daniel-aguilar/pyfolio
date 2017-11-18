from django.conf.urls import url

from .views import (DataTablesLanguageFile, MedicalRecordCreate,
                    MedicalRecordUpdate, PatientCreate, PatientDelete,
                    PatientDetail, PatientList, PatientListApi, PatientUpdate)

app_name = 'emr'
urlpatterns = [
    # API
    url(r'^api/patients/$', PatientListApi.as_view(), name='api-patient-list'),
    url(r'^api/datatables/language/$', DataTablesLanguageFile.as_view(), name='api-datatables-language'),

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
