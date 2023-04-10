from django.urls import path

from .views import (DataTablesLanguageFile, MedicalRecordCreate, MedicalRecordUpdate, PatientCreate, PatientDelete,
                    PatientDetail, PatientList, PatientListApi, PatientUpdate)

app_name = 'emr'
urlpatterns = [
    # API
    path('api/patients/', PatientListApi.as_view(), name='api-patient-list'),
    path('api/datatables/language/', DataTablesLanguageFile.as_view(), name='api-datatables-language'),

    # Patients
    path('patients/', PatientList.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetail.as_view(), name='patient-detail'),
    path('patients/create/', PatientCreate.as_view(), name='patient-create'),
    path('patients/update/<int:pk>/', PatientUpdate.as_view(), name='patient-update'),
    path('patients/delete/<int:pk>/', PatientDelete.as_view(), name='patient-delete'),

    # Medical Records
    path('medical-records/create/<int:patient_pk>/', MedicalRecordCreate.as_view(), name='medical-record-create'),
    path('medical-records/update/<int:pk>/', MedicalRecordUpdate.as_view(), name='medical-record-update'),
]
